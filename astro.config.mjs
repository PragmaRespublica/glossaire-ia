// @ts-check
import { defineConfig } from 'astro/config';
import pagefind from 'astro-pagefind';
import sitemap from '@astrojs/sitemap';

// URL actuelle : https://pragmarespublica.github.io/glossaire-ia/
// Bascule vers glossaire.pragmaforma.com : SITE = 'https://glossaire.pragmaforma.com'
// et BASE = '' · voir INTEGRATION.md pour la procédure complète.
const SITE = 'https://pragmarespublica.github.io';
const BASE = '/glossaire-ia';

export default defineConfig({
  site: SITE,
  base: BASE || '/',
  trailingSlash: 'ignore',
  // CSS inliné dans chaque page : évite la page « nue » quand un HTML en cache
  // (GitHub Pages, max-age=600) référence un CSS haché supprimé par un déploiement.
  build: {
    inlineStylesheets: 'always',
  },
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: true,
    },
  },
  integrations: [
    pagefind(),
    sitemap({
      // La racine est une redirection vers /fr/ : inutile dans le sitemap.
      filter: (page) => new URL(page).pathname !== `${BASE}/`,
      i18n: {
        defaultLocale: 'fr',
        locales: { fr: 'fr-FR', en: 'en-US' },
      },
    }),
  ],
});
