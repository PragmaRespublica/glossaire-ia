# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Bilingual (FR/EN) AI glossary for PragmaForma (~491 terms), built as a fully static Astro site and deployed to GitHub Pages at `https://pragmarespublica.github.io/glossaire-ia/`. French is the primary language; English is a fallback translation. Requires Node >= 22.12.

## Commands

```sh
npm install                        # install dependencies
astro dev --background             # dev server (ALWAYS use background mode)
npm run build                      # static build to ./dist + Pagefind search index
npm run preview                    # preview the production build
python3 scripts/quality-gates.py   # content quality gates (run before committing content changes)
```

Manage the background dev server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

There is no test suite or linter. The quality gates script is the CI check: the deploy workflow (`.github/workflows/deploy.yml`) runs `quality-gates.py` then `npm run build` on every push to `main`, and fails the deploy if either fails.

## Architecture

### Content model (the core of the project)

- Each glossary term is one JSON file in `src/content/termes/<slug>.json`; the slug is the filename. The zod schema lives in `src/content.config.ts` (collection `termes`) and is the single source of truth for the shape and the enums (`AXES`, `NIVEAUX`, `THEMES`, `PAGES_LIEES`, `STATUTS`).
- Text fields come in parallel FR/EN pairs (`definition_fr`/`definition_en`, `exemple_fr`, `regard_fr`, etc.). FR is mandatory; when an EN field is empty, pages fall back to the FR content.
- Terms have a review lifecycle via `statut`: `brouillon` → `a_relire` → `valide`.
- `data/liste-canonique.{csv,json}` is the canonical list of all planned terms; `termes_lies` slugs must point to it (enforced by quality gates).

### Rendering

- Routes: `src/pages/index.astro` redirects to `/fr/`; `src/pages/[lang]/index.astro` renders the A–Z index with filters; `src/pages/[lang]/terme/[slug].astro` renders a term page. Both languages are statically generated for every term.
- UI strings and enum display labels (`AXE_LABELS`, `NIVEAU_LABELS`, `THEME_LABELS`) are in `src/i18n/ui.ts` — add labels there when adding an enum value.
- Search is `astro-pagefind`; the index is built during `npm run build` (term pages are tagged `data-pagefind-body` with filters).
- The site is served under the `/glossaire-ia` base path: always prefix internal URLs with `import.meta.env.BASE_URL` (see existing pages for the pattern).
- Styles: design tokens extracted from pragmaforma.com in `src/styles/tokens.css`, global styles in `src/styles/global.css`; term pages use scoped `<style>` blocks.

### Content pipeline (Python scripts, no dependencies beyond stdlib)

Content is produced in batches through `scripts/`, not written by hand directly into `src/content/termes/`:

1. `scripts/build_liste_canonique.py` — builds `data/liste-canonique.{csv,json}` from published fiches + curated term lists (`data/nouveaux_termes_*.py`).
2. `scripts/generer_fiches.py` — generates term JSONs from the canonical list + writing batches in `data/redaction/*.json`. It never overwrites an existing fiche, and only accepts source URLs listed in `data/redaction/urls-verifiees.txt`.
3. `scripts/apply_translations.py` — applies EN translations from `translations/en-batch*.json`; never touches FR fields.
4. `scripts/illustrations/build.py` — renders the conceptual SVG illustrations to `public/illustrations/<slug>.svg` and the bilingual alt-text manifest `src/data/illustrations.json`. Illustrations are defined as recipes in `scripts/illustrations/recipes_*.py` (each module exports `R: {slug: (draw_fn, alt_fr, alt_en)}`) using the primitives in `primitives.py`.
5. `scripts/quality-gates.py` — blocking checks on every fiche; also writes `rapport-completude.json` (completeness dashboard).
6. `scripts/migrate.py` — one-time migration of the original 80 fiches from the HTML snapshot in `sources/`; kept for reference.

## Content conventions (enforced by quality gates)

- **No em-dash (`—`) anywhere** in content — the editorial charte replaces it with ` · `. This is a blocking CI check.
- Required non-empty fields per fiche: `terme_fr`, `terme_en`, `axe`, `niveau`, `theme`, `definition_fr`, `exemple_fr`, `regard_fr`, `statut`.
- No duplicate `terme_fr`/`terme_en` across fiches (accent- and case-insensitive).
- French UI copy and content use vouvoiement.

## Documentation

Full Astro documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
