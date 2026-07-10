#!/usr/bin/env python3
"""
Portes de qualité automatiques du glossaire (brief §7).

Vérifie sur chaque fiche de src/content/termes/ :
  1. charte : aucun tiret cadratin (—) nulle part ;
  2. champs obligatoires présents et non vides (le schéma zod d'Astro
     valide déjà les types au build · ici on contrôle le contenu) ;
  3. déduplication : pas de doublon de terme_fr / terme_en (insensible
     aux accents et à la casse) ;
  4. score de complétude par fiche (0 à 100) ;
  5. cohérence des termes_lies (chaque slug cible existe).

Sortie : rapport sur stdout + code retour 1 si une porte bloquante échoue.
Écrit aussi rapport-completude.json (utilisé par le tableau de bord de relecture).
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMES = ROOT / "src" / "content" / "termes"
RAPPORT = ROOT / "rapport-completude.json"

OBLIGATOIRES = ["terme_fr", "terme_en", "axe", "niveau", "theme",
                "definition_fr", "exemple_fr", "regard_fr", "statut"]


def norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c)).strip()


def completude(d: dict) -> int:
    """Score 0-100 : contenu FR (40) + EN (30) + enrichissements (30)."""
    score = 0
    score += 10 if d["definition_fr"] else 0
    score += 10 if d["exemple_fr"] else 0
    score += 10 if d["regard_fr"] else 0
    score += 10 if d["sources"] else 0
    score += 10 if d["definition_en"] else 0
    score += 10 if d["exemple_en"] else 0
    score += 10 if d["regard_en"] else 0
    score += 10 if d["schema"]["type"] != "none" else 0
    score += 10 if d["video"] or d["articles"] else 0
    score += 10 if d["termes_lies"] else 0
    return score


def main() -> int:
    erreurs = []
    fiches = {}
    for f in sorted(TERMES.glob("*.json")):
        fiches[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    if not fiches:
        print("ERREUR : aucune fiche trouvée", file=sys.stderr)
        return 1

    # 1 · cadratins
    for slug, d in fiches.items():
        if "—" in json.dumps(d, ensure_ascii=False):
            erreurs.append(f"[cadratin] {slug} contient un tiret cadratin")

    # 2 · champs obligatoires
    for slug, d in fiches.items():
        for champ in OBLIGATOIRES:
            if not d.get(champ):
                erreurs.append(f"[champ vide] {slug}.{champ}")

    # 3 · déduplication
    vus = {}
    for slug, d in fiches.items():
        for champ in ("terme_fr", "terme_en"):
            cle = (champ, norm(d[champ]))
            if cle in vus:
                erreurs.append(f"[doublon] {slug}.{champ} = {vus[cle]}.{champ}")
            vus[cle] = slug

    # 4 · complétude
    scores = {slug: completude(d) for slug, d in fiches.items()}

    # 5 · termes_lies pointent vers des fiches existantes
    for slug, d in fiches.items():
        for cible in d["termes_lies"]:
            if cible not in fiches:
                erreurs.append(f"[terme lié inexistant] {slug} → {cible}")

    RAPPORT.write_text(
        json.dumps(
            {
                slug: {"score": scores[slug], "statut": fiches[slug]["statut"]}
                for slug in sorted(fiches)
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    n = len(fiches)
    moyen = sum(scores.values()) / n
    statuts = {}
    for d in fiches.values():
        statuts[d["statut"]] = statuts.get(d["statut"], 0) + 1
    print(f"Fiches               : {n}")
    print(f"Complétude moyenne   : {moyen:.0f}/100")
    print(f"Statuts              : {statuts}")
    print(f"Score max            : {max(scores, key=scores.get)} ({max(scores.values())})")
    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) :")
        for e in erreurs:
            print(f"  {e}")
        return 1
    print("\nToutes les portes de qualité passent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
