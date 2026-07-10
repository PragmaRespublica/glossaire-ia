# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème données."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, points, bars, meter
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("donnees-entrainement", lambda c: flow(c, "données d'entraînement", ["corpus", "modèle", "capacités + biais"], "un modèle ne vaut jamais mieux que ses données"),
    "Les données d'entraînement déterminent capacités et biais du modèle.",
    "Training data determines the model's capabilities and biases.")
add("jeu-donnees", lambda c: layers(c, "jeu de données", [("ENTRAÎNEMENT", INK), ("VALIDATION", GOLD), ("TEST", POS)], "séparation stricte = score honnête"),
    "Un dataset se sépare strictement en entraînement, validation et test.",
    "A dataset is strictly split into training, validation and test.")
add("donnees-personnelles", lambda c: shield(c, "donnée personnelle", "IDENTIFIE\nUNE PERSONNE", "→ soumise au RGPD"),
    "Toute information permettant d'identifier une personne relève du RGPD.",
    "Any information identifying a person falls under the GDPR.")
add("donnees-sensibles", lambda c: shield(c, "données sensibles", "SANTÉ · ORIGINE\nOPINIONS", "protection renforcée"),
    "Catégories particulières (santé, origine…) à protection renforcée.",
    "Special categories (health, origin…) with reinforced protection.")
add("anonymisation", lambda c: compare(c, "anonymisation", ("noms retirés", "réidentifiable"), ("vraiment anonyme", "irréversible"), "souvent, ce n'est que de la pseudonymisation", winner="right"),
    "L'anonymisation réelle rend la réidentification impossible, ce qui est difficile.",
    "Real anonymisation makes re-identification impossible, which is hard.")
add("pseudonymisation", lambda c: beforeafter(c, "pseudonymisation", "Jean Dupont", ("id: 7X4K", None), "réversible → reste soumise au RGPD"),
    "Remplacer les identifiants par des pseudonymes, de façon réversible.",
    "Replacing identifiers with pseudonyms, reversibly.")
add("minimisation", lambda c: compare(c, "minimisation des données", ("tout collecter", "risque"), ("le nécessaire", "sobre"), "de quelles données ai-je vraiment besoin ?", winner="right"),
    "Ne collecter que les données strictement nécessaires à la finalité.",
    "Collecting only the data strictly necessary for the purpose.")
add("gouvernance-donnees", lambda c: flow(c, "gouvernance des données", ["propriété", "qualité", "cycle de vie"], "l'IA révèle l'état réel du patrimoine de données"),
    "Rôles, processus et règles organisant la gestion des données.",
    "Roles, processes and rules organising data management.")
add("qualite-donnees", lambda c: flow(c, "qualité des données", [("données ✓", POS), "modèle", ("résultat ✓", POS)], "garbage in, garbage out"),
    "La qualité des données plafonne la performance du modèle.",
    "Data quality caps the model's performance.")
add("megadonnees", lambda c: hub(c, "mégadonnées", "BIG DATA", ["volume", "vélocité", "variété"], "la valeur est dans ce qu'on en extrait"),
    "Des données trop volumineuses, rapides ou variées pour les outils classiques.",
    "Data too voluminous, fast or varied for classic tools.")
add("lac-donnees", lambda c: compare(c, "lac de données", ("gouverné", "actif"), ("abandonné", "marécage"), "sans catalogue, un dépotoir", winner="left"),
    "Un réservoir de données brutes ; sans gouvernance, il tourne au marécage.",
    "A reservoir of raw data; without governance, it becomes a swamp.")
add("entrepot-donnees", lambda c: flow(c, "entrepôt de données", ["sources", "modélisation", "tableaux de bord"], "structuré, fiable, optimisé pour l'analyse"),
    "Base centralisée de données structurées, optimisée pour l'analyse.",
    "Centralised structured database, optimised for analysis.")
add("pipeline-donnees", lambda c: flow(c, "pipeline de données", ["extraction", "nettoyage", "chargement"], "un maillon cassé contamine tout l'aval"),
    "Chaîne automatisée acheminant les données de la source à l'usage.",
    "Automated chain routing data from source to use.")
add("donnees-structurees", lambda c: compare(c, "structuré vs non structuré", ("tableaux", "faciles"), ("texte, images", "80% du savoir"), "l'IA générative exploite le non structuré", winner="right"),
    "Le non structuré (textes, images) concentre l'essentiel du savoir des organisations.",
    "Unstructured data (text, images) holds most of organisations' knowledge.")
add("metadonnees", lambda c: flow(c, "métadonnées", ["auteur", "date", "droits"], "filtrer, tracer, sécuriser un RAG"),
    "Des données décrivant d'autres données : auteur, date, droits, source.",
    "Data describing other data: author, date, rights, source.")
add("donnees-ouvertes", lambda c: flow(c, "données ouvertes", [("data.gouv", POS), "réutilisables", "IA souveraine"], "une matière première gratuite et légale"),
    "Données librement accessibles, ressource clé pour l'IA souveraine.",
    "Freely accessible data, a key resource for sovereign AI.")
add("common-crawl", lambda c: flow(c, "common crawl", ["web scrapé", "corpus", "LLM"], "les trésors et les poisons du web"),
    "L'archive du web qui a nourri les grands modèles de langage.",
    "The web archive that fed large language models.")
add("donnees-synthetiques", lambda c: compare(c, "données synthétiques", ("compléter", "utile"), ("tout remplacer", "effondrement"), "imiter le réel sans le trahir", winner="left"),
    "Des données générées imitant le réel, quand les vraies manquent.",
    "Generated data imitating the real, when real data is scarce.")
add("augmentation-donnees", lambda c: beforeafter(c, "augmentation de données", ("500 images", None), ("+ rotations, bruit", None), "enrichir un jeu limité"),
    "Créer de nouvelles données par transformations des existantes.",
    "Creating new data by transforming existing data.")
add("etiquetage-donnees", lambda c: flow(c, "étiquetage des données", ["donnée brute", "annotation ✓", "vérité de référence"], "le carburant caché de l'IA supervisée"),
    "Attribuer aux données les étiquettes servant de vérité de référence.",
    "Attaching to data the labels serving as reference truth.")
add("travailleurs-clic", lambda c: hub(c, "travailleurs du clic", "MICRO-TÂCHES", ["étiquetage", "modération", "évaluation"], "la face cachée humaine de l'IA"),
    "La main-d'œuvre humaine des micro-tâches derrière l'IA.",
    "The human micro-task workforce behind AI.")
add("donnees-fair", lambda c: layers(c, "données fair", [("Findable", POS), ("Accessible", POS), ("Interoperable", POS), ("Reusable", POS)], "des données prêtes pour l'IA"),
    "Findable, Accessible, Interoperable, Reusable : des données de qualité.",
    "Findable, Accessible, Interoperable, Reusable: quality data.")
add("localisation-donnees", lambda c: compare(c, "localisation des données", ("stockage FR", "?"), ("traitement FR", "!"), "où résident ET où transitent les données", winner="right"),
    "Le lieu de stockage ET de traitement détermine le droit applicable.",
    "The place of storage AND processing determines the applicable law.")
add("portabilite-donnees", lambda c: flow(c, "portabilité des données", ["fournisseur A", "export standard", "fournisseur B"], "mesure votre liberté réelle de partir"),
    "Récupérer ses données dans un format réutilisable pour changer de service.",
    "Retrieving your data in a reusable format to switch service.")
add("interoperabilite", lambda c: flow(c, "interopérabilité", ["système A", "standard ouvert", "système B"], "chaque format ouvert est une porte de sortie"),
    "La capacité de systèmes différents à fonctionner ensemble.",
    "The ability of different systems to work together.")
add("souverainete-donnees", lambda c: boundary(c, "souveraineté des données", ["données +", "modèles"], "qui contrôle les données contrôle l'IA"),
    "Garder ses données sous ses propres lois et son contrôle.",
    "Keeping your data under your own laws and control.")
add("tracabilite-donnees", lambda c: flow(c, "traçabilité (lineage)", ["source", "transformations", "résultat"], "d'où vient ce chiffre ?"),
    "Retracer l'origine et le parcours d'une donnée jusqu'à son usage.",
    "Tracing a datum's origin and journey to its use.")
add("caracteristique", lambda c: hub(c, "caractéristique (feature)", "PRÉDICTION", ["âge", "montant", "fréquence"], "chaque variable mérite : est-ce légitime ?"),
    "Variable mesurable utilisée en entrée d'un modèle.",
    "A measurable variable used as model input.")
add("extraction-caracteristiques", lambda c: beforeafter(c, "extraction de caractéristiques", "données brutes", ("caractéristiques", None), "du savoir-faire manuel à l'apprentissage"),
    "Transformer des données brutes en caractéristiques exploitables.",
    "Transforming raw data into usable features.")
add("reduction-dimension", lambda c: beforeafter(c, "réduction de dimension", ("500 variables", None), ("~10 variables", None), "condenser sans trahir le signal"),
    "Réduire le nombre de variables en préservant l'essentiel.",
    "Reducing the number of variables while preserving the essentials.")
add("vectorisation", lambda c: beforeafter(c, "vectorisation", '"souveraineté"', ("[0.2, -0.7, ...]", None), "un modèle ne manipule que des nombres"),
    "Convertir des données non numériques en vecteurs de nombres.",
    "Converting non-numeric data into vectors of numbers.")
add("exploration-donnees", lambda c: bars(c, "exploration de données", [("produit A", 0.7), ("produit B", 0.65, POS)], "des schémas cachés, sans IA générative"),
    "Découvrir schémas et corrélations cachés dans de grands volumes.",
    "Discovering hidden patterns and correlations in large volumes.")
add("echantillonnage", lambda c: bars(c, "biais d'échantillonnage", [("région A", 0.9), ("région B", 0.15, DIM)], "mon échantillon reflète-t-il la réalité ?"),
    "Un échantillon non représentatif fausse tout le modèle.",
    "An unrepresentative sample skews the whole model.")
add("marecage-donnees", lambda c: compare(c, "marécage de données", ("petit lac propre", "exploitable"), ("grand marécage", "ingérable"), "la quantité ne fait pas la valeur", winner="left"),
    "Un lac de données ingouverné, devenu inexploitable.",
    "An ungoverned data lake, become unusable.")
add("donnees-dormantes", lambda c: beforeafter(c, "données dormantes", ("archives oubliées", None), ("RAG interrogeable", None), "un trésor endormi à réveiller"),
    "Des données stockées mais jamais exploitées, réveillées par l'IA.",
    "Data stored but never used, awakened by AI.")
add("audit-documentaire", lambda c: flow(c, "audit documentaire", ["SharePoint", "audit", "corpus RAG ✓"], "30% obsolète, 15% de données sensibles"),
    "Cartographier les sources internes avant de déployer un RAG.",
    "Mapping internal sources before deploying a RAG.")
add("scraping", lambda c: flow(c, "scraping web", ["sites web", "extraction", "corpus IA"], "l'angle mort éthique de l'IA générative"),
    "L'extraction automatisée de contenus web pour entraîner les modèles.",
    "Automated extraction of web content to train models.")
