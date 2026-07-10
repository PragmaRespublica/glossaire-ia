// @ts-check
import { defineConfig } from 'astro/config';
import pagefind from 'astro-pagefind';

// URL cible : https://pragmarespublica.github.io/glossaire-ia/
// Portable vers un domaine custom ou un hébergeur souverain : changer site/base ici.
export default defineConfig({
  site: 'https://pragmarespublica.github.io',
  base: '/glossaire-ia',
  trailingSlash: 'ignore',
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: true,
    },
  },
  integrations: [pagefind()],
});
