/**
 * Tronque un texte pour une meta description (~155 caractères) en coupant
 * sur une frontière de mot, avec une ellipse propre. Évite les descriptions
 * coupées en plein mot dans les résultats de recherche.
 */
export function metaDescription(texte: string, max = 155): string {
  const propre = texte.trim().replace(/\s+/g, ' ');
  if (propre.length <= max) return propre;
  const coupe = propre.slice(0, max - 1);
  const dernierEspace = coupe.lastIndexOf(' ');
  return `${coupe.slice(0, dernierEspace > 80 ? dernierEspace : max - 1).replace(/[,;:·]$/, '')}…`;
}
