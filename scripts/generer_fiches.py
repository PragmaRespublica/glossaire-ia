#!/usr/bin/env python3
"""
Génère les fiches JSON (src/content/termes/) à partir :
 · des métadonnées de la liste canonique (data/liste-canonique.json) ;
 · du contenu rédigé par lots (data/redaction/*.json).

Format d'un lot : { slug: { definition_fr, definition_en, exemple_fr,
exemple_en, regard_fr, regard_en, sous_titre_fr?, sous_titre_en?,
termes_lies?: [slugs], sources: [{titre, url?, licence?}] } }

Contrôles par fiche : slug présent dans la liste canonique, six champs
texte non vides, aucun cadratin, termes_lies pointant vers la liste
canonique, URLs limitées à l'allowlist vérifiée (data/redaction/urls-verifiees.txt).
Ne réécrit jamais une fiche existante (relecture humaine possible entre lots).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMES = ROOT / "src" / "content" / "termes"
REDACTION = ROOT / "data" / "redaction"

TEXTES = ["definition_fr", "definition_en", "exemple_fr", "exemple_en", "regard_fr", "regard_en"]


def main() -> int:
    canon = {
        r["slug"]: r
        for r in json.loads((ROOT / "data" / "liste-canonique.json").read_text(encoding="utf-8"))
    }
    urls_ok = set()
    allow = REDACTION / "urls-verifiees.txt"
    if allow.exists():
        urls_ok = {l.strip() for l in allow.read_text().splitlines() if l.strip()}

    erreurs, ecrites, sautees = [], 0, 0
    for lot in sorted(REDACTION.glob("b*.json")):
        contenu = json.loads(lot.read_text(encoding="utf-8"))
        for slug, c in contenu.items():
            if slug not in canon:
                erreurs.append(f"[hors liste] {lot.name} : {slug}")
                continue
            cible = TERMES / f"{slug}.json"
            if cible.exists():
                sautees += 1
                continue
            if "—" in json.dumps(c, ensure_ascii=False):
                erreurs.append(f"[cadratin] {slug}")
                continue
            manque = [t for t in TEXTES if not c.get(t)]
            if manque:
                erreurs.append(f"[champs vides] {slug} : {manque}")
                continue
            for lie in c.get("termes_lies", []):
                if lie not in canon:
                    erreurs.append(f"[terme lié hors liste] {slug} → {lie}")
            for s in c.get("sources", []):
                if s.get("url") and s["url"] not in urls_ok:
                    erreurs.append(f"[url non vérifiée] {slug} → {s['url']}")
            if not c.get("sources"):
                erreurs.append(f"[sans source] {slug}")

            meta = canon[slug]
            fiche = {
                "terme_fr": meta["terme_fr"],
                "terme_en": meta["terme_en"],
                "sous_titre_fr": c.get("sous_titre_fr", meta["terme_en"]),
                "sous_titre_en": c.get("sous_titre_en", meta["terme_fr"]),
                "axe": meta["axe"],
                "niveau": meta["niveau"],
                "theme": meta["theme"],
                "pages_liees": [],
                "definition_fr": c["definition_fr"],
                "definition_en": c["definition_en"],
                "exemple_fr": c["exemple_fr"],
                "exemple_en": c["exemple_en"],
                "regard_fr": c["regard_fr"],
                "regard_en": c["regard_en"],
                "schema": {"type": "none", "contenu": "", "alt_fr": "", "alt_en": ""},
                "video": None,
                "articles": [],
                "termes_lies": c.get("termes_lies", []),
                "sources": c.get("sources", []),
                "cta": None,
                "statut": "a_relire",
            }
            cible.write_text(
                json.dumps(fiche, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            ecrites += 1

    total = len(list(TERMES.glob("*.json")))
    print(f"Écrites : {ecrites} · déjà présentes (sautées) : {sautees} · total fiches : {total}/{len(canon)}")
    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) :")
        for e in erreurs:
            print(" ", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
