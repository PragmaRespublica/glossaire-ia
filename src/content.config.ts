import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Modèle de données d'un terme du glossaire (brief §3).
 * Un fichier JSON par terme dans src/content/termes/<slug>.json ·
 * le slug est dérivé du nom de fichier.
 * Champs parallèles fr/en pour le texte, champs partagés pour le reste.
 */

export const AXES = [
  'fondamentaux',
  'responsabilite',
  'souverainete',
  'reglementaire',
  'economie',
] as const;

export const NIVEAUX = ['fondamental', 'intermediaire', 'avance'] as const;

export const THEMES = [
  'architecture-modeles',
  'entrainement-apprentissage',
  'prompting-usage',
  'rag-agents',
  'evaluation-qualite',
  'donnees',
  'impact-environnemental',
  'securite',
  'cadre-juridique',
  'ecosysteme-outils',
] as const;

export const PAGES_LIEES = ['fiars', 'b2b', 'ori', 'ressources'] as const;

export const STATUTS = ['brouillon', 'a_relire', 'valide'] as const;

const lienSchema = z.object({
  titre: z.string(),
  url: z.string().url(),
  source: z.string(),
  langue: z.enum(['fr', 'en']),
});

const termeSchema = z.object({
  terme_fr: z.string().min(1),
  terme_en: z.string().min(1),
  // Sous-titre affiché sous le terme (le « term-aka » du site d'origine ·
  // parfois descriptif, pas toujours l'équivalent dans l'autre langue).
  sous_titre_fr: z.string().default(''),
  sous_titre_en: z.string().default(''),
  axe: z.enum(AXES),
  niveau: z.enum(NIVEAUX),
  theme: z.enum(THEMES),
  pages_liees: z.array(z.enum(PAGES_LIEES)).default([]),
  definition_fr: z.string().min(1),
  definition_en: z.string().default(''),
  exemple_fr: z.string().default(''),
  exemple_en: z.string().default(''),
  regard_fr: z.string().default(''),
  regard_en: z.string().default(''),
  schema: z
    .object({
      type: z.enum(['mermaid', 'svg', 'none']),
      contenu: z.string().default(''),
      alt_fr: z.string().default(''),
      alt_en: z.string().default(''),
    })
    .default({ type: 'none', contenu: '', alt_fr: '', alt_en: '' }),
  video: lienSchema.nullable().default(null),
  articles: z.array(lienSchema).default([]),
  termes_lies: z.array(z.string()).default([]),
  sources: z
    .array(
      z.object({
        titre: z.string(),
        url: z.string().url().optional(),
        licence: z.string().optional(),
      })
    )
    .default([]),
  // Bloc « page liée » du site existant : phrase d'accroche + libellé du lien.
  // Préservé tel quel à la migration · nullable pour les nouvelles fiches.
  cta: z
    .object({
      texte_fr: z.string(),
      texte_en: z.string().default(''),
      label_fr: z.string(),
      label_en: z.string().default(''),
      url: z.string(),
    })
    .nullable()
    .default(null),
  statut: z.enum(STATUTS).default('brouillon'),
});

export type Terme = z.infer<typeof termeSchema>;

const termes = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/termes' }),
  schema: termeSchema,
});

export const collections = { termes };
