# Intégration du glossaire sur pragmaforma.com

Objectif : servir ce glossaire sur **https://glossaire.pragmaforma.com** tout en
gardant le déploiement automatique GitHub Pages (chaque push sur `main` publie).

Le site est 100 % statique et autonome : CSS inliné dans chaque page, polices
auto-hébergées (aucun appel à Google Fonts ni à aucun service tiers), recherche
Pagefind embarquée. Aucun serveur applicatif, aucune base de données.

## Pourquoi un sous-domaine (et pas une iframe ni un copier-coller)

- **Iframe : à proscrire.** Google n'indexe pas le contenu iframé au profit du
  site hôte : les ~1000 pages n'apporteraient rien au SEO de pragmaforma.com.
- **Copie des fichiers dans le site principal :** fonctionne, mais chaque mise à
  jour du glossaire exigerait un nouveau dépôt manuel de ~1000 fichiers.
- **Sous-domaine pointé vers GitHub Pages :** une seule entrée DNS, HTTPS
  automatique, mises à jour sans intervention, et tout le capital SEO revient à
  pragmaforma.com (un sous-domaine appartient au domaine).

## Étape 1 · DNS (à faire par vous)

Chez le registrar / gestionnaire DNS de pragmaforma.com, créer :

| Type  | Nom (hôte)  | Valeur                        |
|-------|-------------|-------------------------------|
| CNAME | `glossaire` | `pragmarespublica.github.io.` |

TTL par défaut. Ne pas mettre de proxy/CDN devant (si Cloudflare : mode « DNS
only » le temps que le certificat GitHub soit émis).

## Étape 2 · Déclarer le domaine côté GitHub (Pierre ou vous)

Sur https://github.com/PragmaRespublica/glossaire-ia → Settings → Pages :

1. Custom domain : `glossaire.pragmaforma.com` → Save.
2. Attendre la vérification DNS puis cocher **Enforce HTTPS** (le certificat
   peut prendre jusqu'à ~1 h après la propagation DNS).

Équivalent en ligne de commande :

```bash
gh api repos/PragmaRespublica/glossaire-ia/pages -X PUT -f cname=glossaire.pragmaforma.com
```

## Étape 3 · Basculer la config du site (Pierre / Claude)

Dans `astro.config.mjs`, deux constantes à changer :

```js
const SITE = 'https://glossaire.pragmaforma.com';
const BASE = '';
```

Puis commit + push : le déploiement régénère automatiquement les URL
canoniques, le sitemap, le robots.txt, les hreflang et les balises Open Graph
sur le nouveau domaine. **Ne pas faire cette étape avant que le DNS (étape 1)
soit en place**, sinon le site vivrait quelques heures avec des canonicals
pointant vers un domaine qui ne répond pas encore.

## Étape 4 · Vérifications après bascule

- https://glossaire.pragmaforma.com/fr/ s'affiche avec le style complet ;
- https://glossaire.pragmaforma.com/fr/terme/rag/ idem ;
- https://glossaire.pragmaforma.com/robots.txt répond (désormais à la racine,
  donc actif) et pointe vers le sitemap ;
- https://glossaire.pragmaforma.com/sitemap-index.xml répond ;
- l'ancienne adresse `pragmarespublica.github.io/glossaire-ia/...` redirige en
  301 vers le nouveau domaine (automatique côté GitHub Pages : le jus SEO des
  éventuels liens existants est transféré).

## Étape 5 · SEO côté pragmaforma.com (à faire par vous)

1. **Google Search Console** : ajouter la propriété `glossaire.pragmaforma.com`
   (ou une propriété de domaine `pragmaforma.com` qui couvre tout) et soumettre
   `https://glossaire.pragmaforma.com/sitemap-index.xml`.
2. **Maillage interne** : ajouter un lien « Glossaire IA » dans la navigation
   et/ou le pied de page de pragmaforma.com — c'est le signal le plus fort pour
   que Google associe le glossaire au site.
3. **Liens profonds** : dans les pages et articles de pragmaforma.com, lier les
   termes techniques vers leur fiche (`https://glossaire.pragmaforma.com/fr/terme/rag/`
   par exemple). Quelques liens contextuels valent mieux qu'un lien unique.
4. Le glossaire pointe déjà vers pragmaforma.com (header, footer, CTA de
   fiches) : le maillage est bidirectionnel.

## Ce qui est déjà en place dans le glossaire

- CSS inliné dans chaque page (aucune dépendance à un fichier externe) ;
- polices Inter auto-hébergées (RGPD : aucun appel à Google Fonts) ;
- balises canoniques absolues + hreflang fr/en/x-default sur chaque page ;
- sitemap XML (984 URLs, annotations hreflang) + robots.txt généré ;
- Open Graph + Twitter Cards avec image de partage `og-image.png`
  (régénérer : `node scripts/og-image.mjs`) ;
- données structurées JSON-LD : `DefinedTerm` + fil d'Ariane sur chaque fiche,
  `DefinedTermSet` sur les pages d'accueil ;
- meta descriptions coupées sur frontière de mot (~155 caractères).
