#!/usr/bin/env python3
"""
Applique les traductions EN (translations/en-batch*.json) aux fiches
de src/content/termes/. Ne touche jamais aux champs FR.

Contrôles : couverture complète (chaque fiche non traduite doit être
couverte), aucun cadratin dans les traductions, CTA cohérent (texte EN
fourni si et seulement si la fiche a un CTA).
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TERMES = ROOT / "src" / "content" / "termes"
TRAD = ROOT / "translations"


def main() -> int:
    translations = {}
    for f in sorted(TRAD.glob("en-batch*.json")):
        batch = json.loads(f.read_text(encoding="utf-8"))
        for slug, t in batch.items():
            if slug in translations:
                print(f"ERREUR : {slug} présent dans deux lots", file=sys.stderr)
                return 1
            translations[slug] = t

    erreurs, appliquees = [], 0
    for fiche_path in sorted(TERMES.glob("*.json")):
        slug = fiche_path.stem
        d = json.loads(fiche_path.read_text(encoding="utf-8"))

        if d["definition_en"]:
            continue  # déjà traduite (fiche or, etc.)

        t = translations.get(slug)
        if not t:
            erreurs.append(f"[non couverte] {slug}")
            continue

        if "—" in json.dumps(t, ensure_ascii=False):
            erreurs.append(f"[cadratin] {slug}")
            continue

        for champ in ("sous_titre_en", "definition_en", "exemple_en", "regard_en"):
            if not t.get(champ):
                erreurs.append(f"[vide] {slug}.{champ}")

        if d["cta"] and not t.get("cta_texte_en"):
            erreurs.append(f"[cta manquant] {slug}")
        if not d["cta"] and t.get("cta_texte_en"):
            erreurs.append(f"[cta orphelin] {slug}")

        d["sous_titre_en"] = t["sous_titre_en"]
        d["definition_en"] = t["definition_en"]
        d["exemple_en"] = t["exemple_en"]
        d["regard_en"] = t["regard_en"]
        if d["cta"]:
            d["cta"]["texte_en"] = t["cta_texte_en"]
            d["cta"]["label_en"] = t["cta_label_en"]

        fiche_path.write_text(
            json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        appliquees += 1

    print(f"Traductions appliquées : {appliquees}")
    print(f"Lots chargés           : {len(translations)} entrées")
    if erreurs:
        print(f"\n{len(erreurs)} ERREUR(S) :")
        for e in erreurs:
            print(f"  {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
