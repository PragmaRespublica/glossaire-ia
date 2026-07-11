import type { APIRoute } from 'astro';

// robots.txt généré avec l'URL du sitemap dérivée de site/base : rien à
// modifier lors de la bascule de domaine. Note : un robots.txt n'a d'effet
// qu'à la racine d'un domaine · il devient pleinement actif une fois le site
// servi sur glossaire.pragmaforma.com (base « / »).
export const GET: APIRoute = ({ site }) => {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  const sitemap = new URL(`${base}/sitemap-index.xml`, site).href;
  return new Response(`User-agent: *\nAllow: /\n\nSitemap: ${sitemap}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
