// Génère public/og-image.png (1200×630) · carte de partage social du glossaire.
// Style blueprint de la charte : fond charcoal, tracés orange, monospace.
// Régénérer : node scripts/og-image.mjs (après ajout massif de termes, pour le compteur).
import { readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import sharp from 'sharp';

const racine = join(dirname(fileURLToPath(import.meta.url)), '..');
const nbTermes = readdirSync(join(racine, 'src/content/termes')).filter((f) =>
  f.endsWith('.json')
).length;

const sans = "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif";
const mono = "'SF Mono', Menlo, 'Courier New', monospace";

const svg = `<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <rect width="1200" height="630" fill="#1a1b1c"/>
  <!-- Cadre blueprint -->
  <rect x="36" y="36" width="1128" height="558" fill="none" stroke="#f65009" stroke-opacity="0.35" stroke-width="1.5"/>
  <rect x="44" y="44" width="1112" height="542" fill="none" stroke="#f65009" stroke-opacity="0.12" stroke-width="1"/>

  <!-- Motif blueprint décoratif : docs → recherche → llm -->
  <g stroke="#f65009" stroke-width="2" fill="none" opacity="0.5">
    <rect x="790" y="430" width="100" height="52" rx="6"/>
    <path d="M 890 456 L 934 456 M 926 450 L 934 456 L 926 462"/>
    <rect x="934" y="430" width="100" height="52" rx="6"/>
    <path d="M 1034 456 L 1078 456 M 1070 450 L 1078 456 L 1070 462"/>
    <rect x="1078" y="424" width="10" height="64" rx="4"/>
  </g>
  <g font-family="${mono}" font-size="15" fill="#fa6a2c" opacity="0.75" text-anchor="middle">
    <text x="840" y="461">DOCS</text>
    <text x="984" y="461">SENS</text>
  </g>

  <!-- Eyebrow -->
  <rect x="96" y="108" width="176" height="44" rx="22" fill="none" stroke="#f65009" stroke-width="1.5"/>
  <text x="184" y="136" font-family="${mono}" font-size="18" letter-spacing="4" fill="#fa6a2c" text-anchor="middle">GLOSSAIRE</text>

  <!-- Titre -->
  <text x="96" y="248" font-family="${sans}" font-size="68" font-weight="700" fill="#f0ebe2">Les mots de l&#8217;IA,</text>
  <text x="96" y="330" font-family="${sans}" font-size="68" font-weight="700" font-style="italic" fill="#fa6a2c">définis pour être utilisés.</text>

  <!-- Sous-titre -->
  <text x="96" y="404" font-family="${sans}" font-size="28" fill="#b8b2a6">${nbTermes} termes · Français / English · définitions, exemples, regard critique</text>

  <!-- Pied : marque -->
  <text x="96" y="516" font-family="${sans}" font-size="40" font-weight="700" fill="#f0ebe2">Pragma<tspan fill="#f65009">Forma</tspan></text>
  <text x="96" y="552" font-family="${sans}" font-size="21" fill="#7d7870">Comprendre pour reprendre le pouvoir</text>
</svg>`;

await sharp(Buffer.from(svg)).png().toFile(join(racine, 'public/og-image.png'));
console.log(`✓ public/og-image.png généré (${nbTermes} termes)`);
