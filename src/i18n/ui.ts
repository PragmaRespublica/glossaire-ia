export type Lang = 'fr' | 'en';

export const LANGS: Lang[] = ['fr', 'en'];

/** Libellés d'interface, bilingues. Vouvoiement systématique en français. */
export const ui = {
  fr: {
    'site.title': 'Glossaire IA · PragmaForma',
    'site.tagline': 'Comprendre pour reprendre le pouvoir',
    'nav.back': '← pragmaforma.com',
    'nav.home': 'Accueil',
    'hero.eyebrow': 'Glossaire',
    'hero.title.before': "Les mots de l'IA, ",
    'hero.title.em': 'définis pour être utilisés.',
    'hero.lede':
      "Token, RAG, AI Act, fine-tuning, ACV, agents, vibe coding : derrière chaque terme se cache un enjeu concret. Ce glossaire propose une définition, un exemple d'usage, une perspective PragmaForma et des ressources pour aller plus loin. Toujours sous l'angle responsable et souverain.",
    'count.terms': 'termes · Mise à jour régulière au fil des évolutions du domaine',
    'block.example': 'Exemple concret',
    'block.regard': 'Le regard PragmaForma',
    'block.schema': 'Schéma',
    'block.video': 'Vidéo',
    'block.articles': 'Pour aller plus loin',
    'block.sources': 'Source :',
    'block.related': 'Voir aussi',
    'term.definition': 'Définition',
    'footer.copyright': '© 2026 PragmaForma · Comprendre pour reprendre le pouvoir',
    'a11y.skip': 'Aller au contenu',
    'a11y.langSwitch': 'Choix de la langue',
  },
  en: {
    'site.title': 'AI Glossary · PragmaForma',
    'site.tagline': 'Understand to take back control',
    'nav.back': '← pragmaforma.com',
    'nav.home': 'Home',
    'hero.eyebrow': 'Glossary',
    'hero.title.before': 'The words of AI, ',
    'hero.title.em': 'defined to be used.',
    'hero.lede':
      'Token, RAG, AI Act, fine-tuning, LCA, agents, vibe coding: behind every term lies a concrete issue. This glossary offers a definition, a usage example, a PragmaForma perspective and resources to go further. Always through a responsible and sovereign lens.',
    'count.terms': 'terms · Updated regularly as the field evolves',
    'block.example': 'Concrete example',
    'block.regard': 'The PragmaForma take',
    'block.schema': 'Diagram',
    'block.video': 'Video',
    'block.articles': 'Further reading',
    'block.sources': 'Source:',
    'block.related': 'See also',
    'term.definition': 'Definition',
    'footer.copyright': '© 2026 PragmaForma · Understand to take back control',
    'a11y.skip': 'Skip to content',
    'a11y.langSwitch': 'Language selection',
  },
} as const;

export type UiKey = keyof (typeof ui)['fr'];

export function t(lang: Lang, key: UiKey): string {
  return ui[lang][key];
}

/** Libellés des facettes, bilingues. */
export const AXE_LABELS: Record<string, { fr: string; en: string; css: string }> = {
  fondamentaux: { fr: 'Fondamentaux', en: 'Fundamentals', css: 'axis-fond' },
  responsabilite: { fr: 'Responsabilité', en: 'Responsibility', css: 'axis-resp' },
  souverainete: { fr: 'Souveraineté', en: 'Sovereignty', css: 'axis-souv' },
  reglementaire: { fr: 'Réglementaire', en: 'Regulatory', css: 'axis-reg' },
  economie: { fr: 'Économie', en: 'Economics', css: 'axis-eco' },
};

export const NIVEAU_LABELS: Record<string, { fr: string; en: string }> = {
  fondamental: { fr: 'Fondamental', en: 'Foundational' },
  intermediaire: { fr: 'Intermédiaire', en: 'Intermediate' },
  avance: { fr: 'Avancé', en: 'Advanced' },
};

export const THEME_LABELS: Record<string, { fr: string; en: string }> = {
  'architecture-modeles': { fr: 'Architecture & modèles', en: 'Architecture & models' },
  'entrainement-apprentissage': { fr: 'Entraînement & apprentissage', en: 'Training & learning' },
  'prompting-usage': { fr: 'Prompting & usage', en: 'Prompting & usage' },
  'rag-agents': { fr: 'RAG & agents', en: 'RAG & agents' },
  'evaluation-qualite': { fr: 'Évaluation & qualité', en: 'Evaluation & quality' },
  donnees: { fr: 'Données', en: 'Data' },
  'impact-environnemental': { fr: 'Impact environnemental', en: 'Environmental impact' },
  securite: { fr: 'Sécurité', en: 'Security' },
  'cadre-juridique': { fr: 'Cadre juridique', en: 'Legal framework' },
  'ecosysteme-outils': { fr: 'Écosystème & outils', en: 'Ecosystem & tools' },
};

export const PAGE_LIEE_LABELS: Record<string, { fr: string; en: string }> = {
  fiars: { fr: 'Formation FIARS', en: 'FIARS training' },
  b2b: { fr: 'Offres B2B', en: 'B2B offers' },
  ori: { fr: 'Atelier ORI-IA', en: 'ORI-IA workshop' },
  ressources: { fr: 'Ressources', en: 'Resources' },
};
