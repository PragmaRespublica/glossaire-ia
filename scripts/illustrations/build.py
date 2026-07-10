#!/usr/bin/env python3
"""
Rendu des illustrations conceptuelles vers public/illustrations/<slug>.svg
+ manifeste alt bilingue vers src/data/illustrations.json.

Charge toutes les recettes des modules recipes_*.py (dict R : slug -> (fn, alt_fr, alt_en)),
vérifie que chaque slug existe dans la liste canonique, et rend le SVG.
"""
import importlib
import json
import pkgutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))

from primitives import Canvas  # noqa: E402

OUT = ROOT / "public" / "illustrations"
MANIFEST = ROOT / "src" / "data" / "illustrations.json"


def load_recipes() -> dict:
    recipes = {}
    for mod in pkgutil.iter_modules([str(HERE)]):
        if mod.name.startswith("recipes_"):
            m = importlib.import_module(mod.name)
            for slug, val in getattr(m, "R", {}).items():
                if slug in recipes:
                    print(f"ATTENTION : {slug} défini deux fois", file=sys.stderr)
                recipes[slug] = val
    return recipes


def main() -> int:
    canon = {r["slug"] for r in json.loads((ROOT / "data" / "liste-canonique.json").read_text())}
    recipes = load_recipes()
    OUT.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)

    manifest, erreurs, n = {}, [], 0
    for slug, (fn, alt_fr, alt_en) in sorted(recipes.items()):
        if slug not in canon:
            erreurs.append(f"[hors liste] {slug}")
            continue
        if not alt_fr or not alt_en:
            erreurs.append(f"[alt manquant] {slug}")
        c = Canvas()
        try:
            fn(c)
        except Exception as e:  # noqa: BLE001
            erreurs.append(f"[erreur rendu] {slug} : {e}")
            continue
        (OUT / f"{slug}.svg").write_text(c.render(), encoding="utf-8")
        manifest[slug] = {"alt_fr": alt_fr, "alt_en": alt_en}
        n += 1

    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Illustrations rendues : {n} / {len(canon)} termes")
    if erreurs:
        print(f"\n{len(erreurs)} problème(s) :")
        for e in erreurs:
            print(" ", e)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
