#!/usr/bin/env python3
"""
Construit la liste canonique (~500 termes) : 80 fiches publiées +
nouveaux termes curés (data/nouveaux_termes_*.py).

Portes de qualité : unicité des slugs et des termes (FR et EN,
insensible aux accents), enums valides, statistiques d'équilibre.
Recoupement automatique avec les sources ingérées
(data/sources-candidates.json) → colonne « couverture ».

Sorties : data/liste-canonique.csv + data/liste-canonique.json
"""

import csv
import importlib.util
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMES_DIR = ROOT / "src" / "content" / "termes"
DATA = ROOT / "data"

AXES = {"fondamentaux", "responsabilite", "souverainete", "reglementaire", "economie"}
NIVEAUX = {"fondamental", "intermediaire", "avance"}
THEMES = {
    "architecture-modeles", "entrainement-apprentissage", "prompting-usage",
    "rag-agents", "evaluation-qualite", "donnees", "impact-environnemental",
    "securite", "cadre-juridique", "ecosysteme-outils",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def load_lot(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TERMES


def main() -> int:
    rows, erreurs = [], []

    # 1 · fiches déjà publiées
    for f in sorted(TERMES_DIR.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        rows.append({
            "slug": f.stem, "terme_fr": d["terme_fr"], "terme_en": d["terme_en"],
            "axe": d["axe"], "niveau": d["niveau"], "theme": d["theme"],
            "statut": "publie",
        })

    # 2 · nouveaux termes curés
    for lot in sorted(DATA.glob("nouveaux_termes_*.py")):
        for slug, fr, en, axe, niveau, theme in load_lot(lot):
            rows.append({
                "slug": slug, "terme_fr": fr, "terme_en": en,
                "axe": axe, "niveau": niveau, "theme": theme,
                "statut": "a_rediger",
            })

    # 3 · portes de qualité
    vus_slug, vus_fr, vus_en = {}, {}, {}
    for r in rows:
        if r["axe"] not in AXES:
            erreurs.append(f"[axe] {r['slug']} : {r['axe']}")
        if r["niveau"] not in NIVEAUX:
            erreurs.append(f"[niveau] {r['slug']} : {r['niveau']}")
        if r["theme"] not in THEMES:
            erreurs.append(f"[theme] {r['slug']} : {r['theme']}")
        if not re.fullmatch(r"[a-z0-9-]+", r["slug"]):
            erreurs.append(f"[slug] {r['slug']}")
        for champ, vus in (("slug", vus_slug), ("terme_fr", vus_fr), ("terme_en", vus_en)):
            k = norm(r[champ])
            if k in vus:
                erreurs.append(f"[doublon {champ}] {r['slug']} = {vus[k]}")
            vus[k] = r["slug"]

    # 4 · recoupement avec les sources ingérées
    cand = json.loads((DATA / "sources-candidates.json").read_text(encoding="utf-8"))
    index = {}
    for src, termes in cand.items():
        for t in termes:
            if isinstance(t, dict):
                for v in (t.get("fr"), t.get("en")):
                    if v:
                        index.setdefault(norm(v), set()).add(src)
            else:
                index.setdefault(norm(re.sub(r"\(.*?\)|·.*$|:.*$", "", t)), set()).add(src)
    for r in rows:
        srcs = set()
        for champ in ("terme_fr", "terme_en"):
            base = norm(re.sub(r"\(.*?\)|·.*$", "", r[champ]))
            srcs |= index.get(base, set())
        r["couverture"] = " ".join(sorted(srcs))

    # 5 · statistiques
    def compte(champ):
        c = {}
        for r in rows:
            c[r[champ]] = c.get(r[champ], 0) + 1
        return dict(sorted(c.items(), key=lambda x: -x[1]))

    print(f"TOTAL : {len(rows)} termes ({sum(1 for r in rows if r['statut']=='publie')} publiés + {sum(1 for r in rows if r['statut']=='a_rediger')} à rédiger)")
    print("Axes   :", compte("axe"))
    print("Niveaux:", compte("niveau"))
    print("Thèmes :", compte("theme"))
    couverts = sum(1 for r in rows if r["couverture"])
    print(f"Recoupés dans ≥1 source ingérée : {couverts}/{len(rows)}")

    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) :")
        for e in erreurs:
            print(" ", e)
        return 1

    # 6 · exports
    rows.sort(key=lambda r: r["slug"])
    champs = ["slug", "terme_fr", "terme_en", "axe", "niveau", "theme", "statut", "couverture"]
    with open(DATA / "liste-canonique.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=champs)
        w.writeheader()
        w.writerows(rows)
    (DATA / "liste-canonique.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )
    print("\nExports : data/liste-canonique.csv · data/liste-canonique.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
