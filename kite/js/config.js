// ============================================================
// Configuration des spots de kite autour de Marseille.
// Les secteurs de vent sont exprimés en degrés (d'où vient le
// vent, 0 = Nord, 90 = Est…) sous forme de plages [début, fin]
// dans le sens horaire (une plage peut traverser le nord,
// ex. [330, 30]).
//   - secteursIdeaux   : direction franche pour naviguer
//   - secteursCorrects : navigable mais pas optimal (side-off,
//                        vent dévié, clapot…)
//   - tout le reste    : offshore ou impraticable → rouge
// Ajustez ces plages selon votre connaissance des spots !
// ============================================================

const SPOTS = [
  {
    id: "le-jai",
    nom: "Le Jaï",
    commune: "Marignane · étang de Berre",
    lat: 43.4262,
    lon: 5.1917,
    secteursIdeaux: [[280, 350], [100, 150]],   // Mistral NO · vent d'Est-SE
    secteursCorrects: [[250, 280], [150, 180]],
    notes: "Plan d'eau plat, idéal Mistral. Zone kite balisée en été.",
    image: "assets/le-jai.jpg",
  },
  {
    id: "carro",
    nom: "Carro",
    commune: "Martigues · Côte Bleue",
    lat: 43.3296,
    lon: 5.0409,
    secteursIdeaux: [[260, 330]],               // Ouest à Mistral
    secteursCorrects: [[210, 260]],             // Sud-Ouest
    notes: "Spot exposé, vagues possibles. Niveau confirmé conseillé par fort Mistral.",
    image: "assets/carro.jpg",
  },
  {
    id: "pointe-rouge",
    nom: "Pointe Rouge",
    commune: "Marseille 8e",
    lat: 43.2450,
    lon: 5.3720,
    secteursIdeaux: [[210, 280]],               // brise SO-O onshore
    secteursCorrects: [[280, 330], [150, 210]], // Mistral side-off · Sud
    notes: "Pratique réglementée en été (zone et horaires) : vérifier l'arrêté municipal.",
    image: "assets/pointe-rouge.jpg",
  },
  {
    id: "plage-napoleon",
    nom: "Plage Napoléon",
    commune: "Port-Saint-Louis-du-Rhône",
    lat: 43.3746,
    lon: 4.8582,
    secteursIdeaux: [[280, 340], [90, 160]],    // Mistral side-on · Sud-Est
    secteursCorrects: [[180, 280]],
    notes: "Grande plage de sable, très fréquentée par Mistral. Eau peu profonde au bord.",
    image: "assets/plage-napoleon.jpg",
  },
  {
    id: "la-ciotat",
    nom: "La Ciotat",
    commune: "Baie de La Ciotat",
    lat: 43.1740,
    lon: 5.6100,
    secteursIdeaux: [[150, 230]],               // Sud-Est à Sud-Ouest onshore
    secteursCorrects: [[230, 270]],
    notes: "Marche bien par vent d'Est/Sud-Est quand le Mistral ne donne pas.",
    image: "assets/la-ciotat.jpg",
  },
];

// Réglages par défaut du rider (modifiables dans l'écran Reco,
// mémorisés dans le navigateur).
const REGLAGES_DEFAUT = {
  poids: 80,      // kg
  ventMin: 12,    // nœuds — en dessous : pas navigable
  ventMax: 30,    // nœuds — au-dessus : trop fort
};

// Ratio rafales / vent moyen au-delà duquel le vent est jugé
// irrégulier (verdict dégradé d'un cran).
const SEUIL_RAFALES = 1.6;

// Fréquence de rafraîchissement automatique (ms).
const INTERVALLE_MAJ = 5 * 60 * 1000;
