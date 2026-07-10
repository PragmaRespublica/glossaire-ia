# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème entraînement & apprentissage."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, bars
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("apprentissage-supervise", lambda c: flow(c, "apprentissage supervisé", ["exemples étiquetés", "modèle", "généralise"], "l'étiquetage humain plafonne le modèle"),
    "Le modèle apprend à partir d'exemples étiquetés par des humains.",
    "The model learns from human-labelled examples.")
add("apprentissage-non-supervise", lambda c: bars(c, "apprentissage non supervisé", [("segment A", 0.6), ("segment B", 0.45, POS), ("segment C", 0.3, GOLD)], "découvrir des structures cachées"),
    "Le modèle découvre seul des structures dans des données non étiquetées.",
    "The model discovers structures in unlabelled data on its own.")
add("apprentissage-semi-supervise", lambda c: compare(c, "apprentissage semi-supervisé", ("1 000 étiquetés", "guident"), ("1 M non étiquetés", "affinent"), "maximiser une annotation limitée", winner=None),
    "Combiner peu de données étiquetées et beaucoup de non étiquetées.",
    "Combining little labelled data with much unlabelled data.")
add("apprentissage-auto-supervise", lambda c: flow(c, "apprentissage auto-supervisé", ['"le chat ___"', "prédire", "le texte = réponse"], "affranchi de l'annotation humaine"),
    "Le modèle génère ses propres étiquettes à partir de la structure des données.",
    "The model generates its own labels from the data's structure.")
add("apprentissage-renforcement", lambda c: flow(c, "apprentissage par renforcement", ["agir", "récompense", "ajuster"], "tout dépend de la fonction de récompense", loop=True),
    "L'agent apprend par essais et erreurs, guidé par des récompenses.",
    "The agent learns by trial and error, guided by rewards.")
add("apprentissage-transfert", lambda c: beforeafter(c, "apprentissage par transfert", ("modèle général", None), ("+ vos 2000 images", None), "hériter d'un savoir plutôt que le reconstruire"),
    "Réutiliser un modèle entraîné pour l'adapter à une tâche voisine.",
    "Reusing a trained model to adapt it to a related task.")
add("apprentissage-continu", lambda c: compare(c, "apprentissage continu", ("apprendre le neuf", "?"), ("sans oublier", "défi"), "stabilité contre adaptation", winner=None),
    "Apprendre de nouvelles tâches sans oublier les précédentes.",
    "Learning new tasks without forgetting the previous ones.")
add("apprentissage-actif", lambda c: flow(c, "apprentissage actif", ["cas incertains", "faire étiqueter", "apprendre plus"], "1/20e de l'effort d'annotation"),
    "Le modèle choisit les données les plus utiles à faire étiqueter.",
    "The model chooses the most useful data to have labelled.")
add("pre-entrainement", lambda c: flow(c, "préentraînement", ["corpus immense", "auto-supervision", "modèle brut"], "l'affaire de quelques acteurs"),
    "La première phase, où le modèle apprend des connaissances générales.",
    "The first phase, where the model learns general knowledge.")
add("post-entrainement", lambda c: flow(c, "post-entraînement", ["modèle brut", "alignement", "assistant utile"], "là où se logent les valeurs d'un modèle"),
    "Les phases transformant un modèle brut en assistant utile et sûr.",
    "The phases turning a raw model into a useful, safe assistant.")
add("alignement-ia", lambda c: compare(c, "alignement de l'ia", ("demande nuisible", "refuse"), ("utile & honnête", "aligné"), "aligner sur quelles valeurs, par qui ?", winner="right"),
    "Faire agir l'IA conformément aux intentions et valeurs humaines.",
    "Making AI act in accordance with human intentions and values.")
add("ia-constitutionnelle", lambda c: flow(c, "ia constitutionnelle", ["principes", "auto-critique", "réponse alignée"], "des valeurs explicites et débattables"),
    "Guider le modèle par une « constitution » de principes explicites.",
    "Guiding the model with a \"constitution\" of explicit principles.")
add("rlhf", lambda c: flow(c, "rlhf", ["humains classent", "modèle de récompense", "renforcement"], "reflète les préférences des annotateurs"),
    "Aligner un LLM sur les préférences humaines par renforcement.",
    "Aligning an LLM on human preferences through reinforcement.")
add("dpo-optimisation", lambda c: compare(c, "dpo", ("RLHF complet", "lourd"), ("paires préférées", "simple"), "l'alignement accessible à plus d'acteurs", winner="right"),
    "Un alignement plus simple que le RLHF, à partir de paires de réponses.",
    "An alignment simpler than RLHF, from pairs of responses.")
add("lora", lambda c: beforeafter(c, "lora · adaptation à faible rang", ("fine-tuning complet", "GPU coûteux"), ("fine couche", "1 GPU"), "la personnalisation à la portée des PME"),
    "Un fine-tuning économe n'ajustant qu'une fine couche d'adaptation.",
    "An economical fine-tuning adjusting only a thin adaptation layer.")
add("instruction-tuning", lambda c: beforeafter(c, "ajustement par instructions", ('"résume" → suite', None), ('"résume" → résumé', None), "d'un modèle brut à un assistant docile"),
    "Apprendre au modèle à suivre des instructions en langage naturel.",
    "Teaching the model to follow natural-language instructions.")
add("modele-recompense", lambda c: flow(c, "modèle de récompense", ["sorties", "note qualité", "guide l'apprentissage"], "un juge biaisé enseigne mal"),
    "Un modèle auxiliaire prédisant les préférences humaines.",
    "An auxiliary model predicting human preferences.")
add("distillation", lambda c: beforeafter(c, "distillation", ("modèle maître", "gros"), ("modèle élève", "10-50× sobre"), "un levier de sobriété puissant"),
    "Entraîner un petit modèle à reproduire les sorties d'un plus grand.",
    "Training a small model to reproduce a larger one's outputs.")
add("federated-learning", lambda c: boundary(c, "apprentissage fédéré", ["données", "chez chacun"], "seuls les paramètres sont partagés", out="rien ne sort"),
    "Entraîner un modèle sans centraliser les données sensibles.",
    "Training a model without centralising sensitive data.")
add("hyperparametre", lambda c: bars(c, "hyperparamètre", [("réglage A", 0.6), ("réglage B", 0.85, POS)], "choisis par le concepteur, avant l'entraînement"),
    "Un réglage fixé avant l'entraînement, qui en contrôle le déroulement.",
    "A setting fixed before training that controls how it unfolds.")
add("taux-apprentissage", lambda c: meter(c, "taux d'apprentissage", "trop lent", "trop élevé", "avancer assez vite, sans déraper", pos=0.4),
    "L'ampleur des ajustements à chaque étape d'entraînement.",
    "The magnitude of adjustments at each training step.")
add("descente-gradient", lambda c: flow(c, "descente de gradient", ["erreur", "pas vers le bas", "meilleure config"], "une procédure simple, répétée des milliards de fois", loop=True),
    "Ajuster les paramètres dans la direction qui réduit le plus l'erreur.",
    "Adjusting parameters in the direction that most reduces error.")
add("retropropagation", lambda c: flow(c, "rétropropagation", ["erreur en sortie", "remonter les couches", "corriger chaque poids"], "le socle discret de l'IA moderne"),
    "Calculer la contribution de chaque paramètre à l'erreur globale.",
    "Computing each parameter's contribution to the overall error.")
add("fonction-perte", lambda c: flow(c, "fonction de perte", ["prédiction", "écart", "à minimiser"], "elle encode les priorités"),
    "La fonction mesurant l'écart entre prédictions et réponses attendues.",
    "The function measuring the gap between predictions and expected answers.")
add("surapprentissage", lambda c: compare(c, "surapprentissage", ("entraînement", "99%"), ("production", "84%"), "méfiez-vous des modèles trop parfaits", winner=None),
    "Le modèle mémorise ses données au lieu d'en dégager des règles.",
    "The model memorises its data instead of extracting rules.")
add("sous-apprentissage", lambda c: compare(c, "sous-apprentissage", ("modèle trop simple", "échoue partout"), ("plus expressif", "capte"), "diagnostiquer lequel vous menace", winner="right"),
    "Le modèle est trop simple pour capturer les régularités.",
    "The model is too simple to capture the regularities.")
add("regularisation", lambda c: beforeafter(c, "régularisation", ("surapprend", None), ("bridé → généralise", None), "brider un modèle le rend souvent meilleur"),
    "Limiter la complexité d'un modèle pour éviter le surapprentissage.",
    "Limiting a model's complexity to avoid overfitting.")
add("dropout", lambda c: flow(c, "abandon (dropout)", ["neurones", "20% éteints", "plus robuste"], "une astuce simple, redoutablement efficace"),
    "Désactiver aléatoirement des neurones pour un modèle plus robuste.",
    "Randomly deactivating neurons for a more robust model.")
add("generalisation", lambda c: compare(c, "généralisation", ("réciter le vu", "facile"), ("s'adapter à l'inédit", "difficile"), "le vrai juge d'un modèle", winner="right"),
    "Bien se comporter sur des données jamais vues à l'entraînement.",
    "Behaving well on data never seen in training.")
add("epoque", lambda c: meter(c, "époque (epoch)", "trop peu", "trop", "savoir s'arrêter au bon moment", pos=0.5),
    "Un passage complet des données d'entraînement à travers le modèle.",
    "A complete pass of the training data through the model.")
add("corpus-entrainement", lambda c: bars(c, "corpus d'entraînement", [("anglais", 0.9, INK), ("français", 0.2, POS)], "l'ADN culturel d'un modèle"),
    "L'ensemble des textes rassemblés pour entraîner un modèle.",
    "The set of texts gathered to train a model.")
add("desapprentissage", lambda c: flow(c, "désapprentissage machine", ["demande d'effacement", "\"oublier\"", "sans réentraîner"], "le chaînon manquant du droit à l'effacement"),
    "Faire « oublier » à un modèle des données précises.",
    "Making a model \"forget\" specific data.")
add("automl", lambda c: flow(c, "automl", ["données", "tests auto", "bon modèle"], "abaisse la barrière technique, pas la responsabilité"),
    "Automatiser les étapes de construction d'un modèle.",
    "Automating the steps of building a model.")
add("versionnage-modeles", lambda c: flow(c, "versions de modèles", ["v1 stable", "v2 régression", "← retour v1"], "sans historique, ingérable"),
    "Suivre et gérer les versions d'un modèle au fil de son évolution.",
    "Tracking and managing a model's versions as it evolves.")
add("point-controle", lambda c: flow(c, "point de contrôle", ["entraînement long", "sauvegarde", "reprise"], "l'assurance des entraînements coûteux"),
    "Sauvegarder l'état d'un modèle à un instant de son entraînement.",
    "Saving a model's state at a moment of its training.")
add("courbes-apprentissage", lambda c: compare(c, "convergence", ("erreur baisse", "sain"), ("validation remonte", "surapprend"), "le stéthoscope du praticien", winner=None),
    "Suivre l'évolution de l'erreur pour diagnostiquer l'entraînement.",
    "Tracking the error's evolution to diagnose training.")
add("oubli-catastrophique", lambda c: beforeafter(c, "oubli catastrophique", ("compétences générales", None), ("écrasées par le neuf", None), "l'IA écrase, l'humain accumule"),
    "Apprendre du nouveau efface brutalement l'ancien.",
    "Learning the new abruptly erases the old.")
add("effondrement-modele", lambda c: flow(c, "effondrement de modèle", ["IA d'hier", "entraîne", "IA appauvrie"], "photocopie de photocopie", loop=True),
    "Les modèles entraînés en boucle sur du contenu IA s'appauvrissent.",
    "Models trained in a loop on AI content impoverish.")
add("date-coupure", lambda c: compare(c, "date de coupure", ("avant coupure", "sait"), ("après", "ignore / invente"), "coupler à une recherche à jour", winner=None),
    "La date au-delà de laquelle le modèle ignore les événements.",
    "The date beyond which the model is unaware of events.")
add("entrainement", lambda c: flow(c, "entraînement", ["données", "milliards d'ajustements", "modèle"], "très coûteux, une seule fois"),
    "La phase où un modèle apprend à partir d'un jeu de données massif.",
    "The phase where a model learns from a massive dataset.")
