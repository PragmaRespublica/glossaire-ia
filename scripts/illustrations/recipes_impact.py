# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème impact environnemental."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, bars
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("acv", lambda c: flow(c, "analyse du cycle de vie", ["fabrication", "usage", "fin de vie"], "l'inférence dépasse vite l'entraînement"),
    "L'ACV mesure les impacts d'un produit sur tout son cycle de vie.",
    "LCA measures a product's impacts across its whole life cycle.")
add("ademe", lambda c: shield(c, "ademe", "RÉFÉRENTIELS\nPUBLICS", "l'antidote aux bilans autoproclamés"),
    "L'ADEME publie des référentiels d'évaluation d'impact environnemental.",
    "ADEME publishes environmental impact assessment frameworks.")
add("co2eq", lambda c: meter(c, "équivalent co₂", "négligeable", "à l'échelle", "1 à 4 g par requête, ×millions", pos=0.4),
    "Unité agrégeant tous les gaz à effet de serre en équivalent CO₂.",
    "A unit aggregating all greenhouse gases into CO₂ equivalent.")
add("consommation-eau", lambda c: meter(c, "consommation d'eau", "0 L/kWh", "2+ L/kWh", "l'angle mort du débat sur l'IA", pos=0.55),
    "L'eau consommée pour refroidir les data centers, souvent ignorée.",
    "The water consumed to cool data centers, often ignored.")
add("consommation-electrique", lambda c: compare(c, "consommation électrique", ("recherche web", "×1"), ("requête LLM", "×10"), "pour quel service rendu ?", winner=None),
    "Une requête LLM consomme environ 10 fois plus qu'une recherche web.",
    "An LLM request consumes about 10 times more than a web search.")
add("csrd", lambda c: flow(c, "csrd", ["usage IA", "scope 3", "reporting audité"], "l'impact de l'IA devient un sujet de conformité"),
    "La directive européenne de reporting de durabilité, où entre l'IA.",
    "The European sustainability reporting directive, which AI enters.")
add("data-center", lambda c: hub(c, "data center", "SERVEURS", ["électricité", "eau", "chaleur"], "consommation en hausse, tirée par l'IA"),
    "L'infrastructure physique qui exécute l'entraînement et l'inférence.",
    "The physical infrastructure running training and inference.")
add("dechets-electroniques", lambda c: flow(c, "déchets électroniques", ["GPU 3-4 ans", "remplacé", "déchet"], "moins d'un quart correctement recyclé"),
    "Les équipements électroniques en fin de vie, aggravés par l'IA.",
    "End-of-life electronic equipment, worsened by AI.")
add("ecologits", lambda c: bars(c, "ecologits", [("énergie", 0.5), ("CO₂", 0.35), ("eau", 0.6, POS)], "mesurer par la donnée, pas l'intuition"),
    "Une bibliothèque mesurant l'empreinte des appels aux LLM.",
    "A library measuring the footprint of LLM calls.")
add("effet-rebond", lambda c: compare(c, "effet rebond", ("coût/token ÷", "efficace"), ("usage total ×", "explose"), "l'efficacité seule ne suffit pas", winner=None),
    "Les gains d'efficacité augmentent l'usage total au lieu de le réduire.",
    "Efficiency gains increase total use instead of reducing it.")
add("empreinte-materielle", lambda c: layers(c, "empreinte matérielle", [("extraction minerais", INK), ("fabrication puces", INK), ("assemblage", GOLD)], "> 3/4 de l'impact d'un terminal"),
    "L'impact de la fabrication du matériel : minerais, puces, transport.",
    "The impact of hardware manufacturing: minerals, chips, transport.")
add("ia-climat", lambda c: compare(c, "ia au service du climat", ("prévision réseau", "évite +"), ("vidéo 8K", "émet +"), "le bilan net par cas d'usage", winner="left"),
    "L'IA au service du climat : le vrai critère est le bilan net.",
    "AI serving the climate: the real criterion is the net balance.")
add("ia-frugale", lambda c: compare(c, "ia frugale", ("grand modèle", "÷30 conso"), ("petit modèle", "-1% précision"), "le modèle minimal qui suffit", winner="right"),
    "Minimiser les ressources consommées pour un service rendu donné.",
    "Minimising resources consumed for a given service.")
add("intensite-carbone", lambda c: meter(c, "intensité carbone", "FR ~50g", "US ~450g", "×6 à ×8 selon le mix, à conso égale", pos=0.2),
    "Le CO₂ par kWh varie énormément selon le pays et l'heure.",
    "CO₂ per kWh varies enormously by country and hour.")
add("mix-energetique", lambda c: bars(c, "mix énergétique", [("France", 0.95, POS), ("Irlande", 0.4, INK)], "où sont physiquement les serveurs ?"),
    "La répartition des sources d'électricité détermine l'empreinte réelle.",
    "The breakdown of electricity sources determines the real footprint.")
add("neutralite-carbone", lambda c: compare(c, "neutralité carbone", ("annoncée", "slogan"), ("émissions réelles", "+30-50%"), "fiez-vous aux kWh, pas aux slogans", winner=None),
    "Les promesses de neutralité des Big Tech face à la hausse réelle.",
    "Big Tech neutrality pledges against real emission rises.")
add("numerique-responsable", lambda c: hub(c, "numérique responsable", "SOBRIÉTÉ", ["durée de vie", "écoconception", "inclusion"], "raccrochez vos usages IA à cette démarche"),
    "Réduire l'empreinte environnementale et sociale du numérique.",
    "Reducing the environmental and social footprint of digital tech.")
add("obsolescence-materiel", lambda c: compare(c, "obsolescence du matériel", ("renouveler 500 postes", "?"), ("côté serveur", "!"), "l'IA, nouveau prétexte d'obsolescence ?", winner="right"),
    "Le renouvellement accéléré des serveurs et terminaux « pour l'IA ».",
    "The accelerated renewal of servers and devices \"for AI\".")
add("pue", lambda c: meter(c, "power usage effectiveness", "1.1 idéal", "1.5 moyen", "indicateur partiel : ni eau ni fabrication", pos=0.45),
    "L'efficacité énergétique d'un data center : total / informatique.",
    "A data center's energy efficiency: total / IT.")
add("refroidissement", lambda c: compare(c, "refroidissement", ("air", "10 kW"), ("liquide", "120 kW"), "free cooling, récupération de chaleur", winner="right"),
    "Évacuer la chaleur des GPU denses : liquide, immersion, chaleur fatale.",
    "Removing heat from dense GPUs: liquid, immersion, waste-heat reuse.")
add("scope-3", lambda c: layers(c, "émissions scope 3", [("scope 1 · direct", DIM), ("scope 2 · énergie", DIM), ("SCOPE 3 · IA externalisée", INK)], "vous répondez des émissions de vos fournisseurs"),
    "Les émissions indirectes de la chaîne de valeur, dont l'IA consommée.",
    "The value chain's indirect emissions, including consumed AI.")
add("terres-rares", lambda c: hub(c, "terres rares", "PUCES IA", ["gallium", "germanium", "cuivre"], "dépendance géopolitique, Chine dominante"),
    "Les minerais critiques des puces, à forte dépendance géopolitique.",
    "The critical minerals of chips, with high geopolitical dependence.")
add("wue", lambda c: meter(c, "water usage effectiveness", "0.2 L/kWh", "2 L/kWh", "à exiger de vos hébergeurs dès aujourd'hui", pos=0.5),
    "L'efficacité hydrique d'un data center : litres d'eau par kWh.",
    "A data center's water efficiency: litres of water per kWh.")
