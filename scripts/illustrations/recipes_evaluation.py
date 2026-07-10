# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème évaluation & qualité."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, bars
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("mmlu", lambda c: bars(c, "mmlu", [("modèle A", 0.86, INK), ("modèle B", 0.81, POS)], "≠ votre cas d'usage réel"),
    "Un benchmark de culture générale, souvent sur-interprété.",
    "A general-knowledge benchmark, often over-interpreted.")
add("humaneval", lambda c: bars(c, "humaneval", [("fonctions simples", 0.8, INK)], "loin de la complexité d'un vrai projet"),
    "Un benchmark de génération de code sur des fonctions isolées.",
    "A code-generation benchmark on isolated functions.")
add("gpqa", lambda c: bars(c, "gpqa", [("modèle raisonnement", 0.7, POS), ("modèle standard", 0.4, DIM)], "raisonnement de niveau doctorat"),
    "Un benchmark de raisonnement scientifique « à l'épreuve de Google ».",
    "A \"Google-proof\" scientific-reasoning benchmark.")
add("swe-bench", lambda c: bars(c, "swe-bench", [("tickets réels résolus", 0.4, POS)], "des problèmes réels, pas des exercices"),
    "Un benchmark de résolution de vrais problèmes logiciels.",
    "A benchmark of solving real software problems.")
add("arene-llm", lambda c: compare(c, "arène (lmarena)", ("modèle A", "vote ?"), ("modèle B", "vote ?"), "l'utilité perçue par des votes humains", winner=None),
    "Un classement par votes humains comparant deux réponses anonymes.",
    "A human-vote ranking comparing two anonymous answers.")
add("llm-juge", lambda c: flow(c, "llm juge", ["réponses", "LLM note", "tri à grande échelle"], "calibrer sur un échantillon humain"),
    "Utiliser un LLM pour évaluer automatiquement d'autres réponses.",
    "Using an LLM to automatically evaluate other responses.")
add("precision-rappel", lambda c: compare(c, "précision & rappel", ("précision", "peu de faux +"), ("rappel", "rate peu"), "améliorer l'une dégrade l'autre", winner=None),
    "Deux métriques complémentaires : ne pas se tromper, ne rien rater.",
    "Two complementary metrics: not erring, missing nothing.")
add("faux-positifs", lambda c: compare(c, "faux positifs / négatifs", ("fausse alerte", "rattrapable"), ("cas raté", "grave"), "quelle erreur coûte le plus cher ?", winner=None),
    "Les deux types d'erreurs, aux conséquences rarement symétriques.",
    "The two types of errors, with rarely symmetric consequences.")
add("matrice-confusion", lambda c: layers(c, "matrice de confusion", [("vrais positifs", POS), ("faux positifs", GOLD), ("faux négatifs", INK)], "l'antidote au chiffre unique trompeur"),
    "Le tableau croisant prédictions et réalité, où logent les erreurs.",
    "The table crossing predictions and reality, where errors lie.")
add("perplexite-metrique", lambda c: meter(c, "perplexité", "peu surpris", "très surpris", "outil d'ingénieur, pas argument de vente", pos=0.35),
    "Une métrique de « surprise » du modèle, sans dire l'utilité perçue.",
    "A model \"surprise\" metric, not saying perceived usefulness.")
add("rouge-bleu", lambda c: compare(c, "rouge / bleu", ("mêmes mots", "score haut"), ("reformulé", "score bas"), "ressemblance lexicale ≠ qualité", winner=None),
    "Des métriques comparant au texte de référence par recouvrement de mots.",
    "Metrics comparing to a reference text by word overlap.")
add("verite-terrain", lambda c: flow(c, "vérité terrain", ["référence", "juge le modèle", "qui juge le juge ?"], "sa constitution mérite autant de soin"),
    "Les données de référence servant d'étalon, jamais parfaites.",
    "The reference data serving as yardstick, never perfect.")
add("score-confiance", lambda c: compare(c, "score de confiance", ("confiant", "≠"), ("fiable", "?"), "un modèle qui ne doute jamais inquiète", winner=None),
    "L'assurance affichée n'est pas la fiabilité réelle.",
    "Displayed confidence is not real reliability.")
add("explicabilite", lambda c: flow(c, "explicabilité", ["décision", "pourquoi ?", "contestable"], "on ne conteste pas ce qu'on ne comprend pas"),
    "Fournir des explications compréhensibles sur un résultat d'IA.",
    "Providing understandable explanations of an AI result.")
add("interpretabilite", lambda c: flow(c, "interprétabilité", ["boîte noire", "ouvrir", "auditer de l'intérieur"], "la clé de l'IA de confiance à long terme"),
    "Comprendre le fonctionnement interne d'un modèle.",
    "Understanding a model's internal workings.")
add("boite-noire", lambda c: compare(c, "effet boîte noire", ("recommander série", "tolérable"), ("refuser crédit", "inacceptable"), "l'acceptabilité dépend de l'enjeu", winner=None),
    "Des résultats sans que l'on comprenne le raisonnement.",
    "Results without one understanding the reasoning.")
add("transparence-algorithmes", lambda c: flow(c, "transparence des algorithmes", ["critères", "pondération", "publiés"], "une condition de légitimité démocratique"),
    "Rendre compréhensibles la logique et les effets d'un algorithme.",
    "Making an algorithm's logic and effects understandable.")
add("robustesse", lambda c: compare(c, "robustesse", ("en démo", "brille"), ("en production", "tient ?"), "testez sur le réel, pas sur l'idéal", winner=None),
    "Maintenir ses performances face à des conditions imprévues.",
    "Maintaining performance under unforeseen conditions.")
add("derive-modele", lambda c: bars(c, "dérive du modèle", [("2024", 0.9, POS), ("2026", 0.5, INK)], "un modèle oublié se dégrade en silence"),
    "La dégradation progressive des performances en production.",
    "The gradual performance degradation in production.")
add("derive-donnees", lambda c: flow(c, "dérive des données", ["entrée change", "distribution ≠", "alerte"], "surveiller les entrées pour anticiper"),
    "L'évolution des données d'entrée, cause fréquente de dérive.",
    "The evolution of input data, a frequent cause of drift.")
add("equite-algorithmique", lambda c: compare(c, "équité algorithmique", ("même taux d'accept.", "critère A"), ("même taux d'erreur", "critère B"), "un choix de société, pas un réglage", winner=None),
    "Éviter les discriminations injustifiées, sans définition unique.",
    "Avoiding unjustified discrimination, with no single definition.")
add("audit-algorithmique", lambda c: flow(c, "audit algorithmique", ["système", "examen", "rapport ✓"], "découvrir ses failles en privé"),
    "Examiner un système d'IA pour vérifier conformité et équité.",
    "Examining an AI system to verify compliance and fairness.")
add("contamination", lambda c: compare(c, "contamination des benchmarks", ("scores records", "?"), ("test dans l'entraînement", "récite"), "toujours tester sur vos données", winner=None),
    "Les données d'évaluation présentes dans l'entraînement gonflent les scores.",
    "Evaluation data present in training inflates scores.")
add("evaluation-humaine", lambda c: compare(c, "évaluation humaine", ("benchmarks", "départagent peu"), ("utilisateurs métier", "tranchent"), "irremplaçable pour capter la nuance", winner="right"),
    "Des personnes jugent la qualité réelle des sorties.",
    "People judge the real quality of outputs.")
add("evaluation-agents", lambda c: compare(c, "évaluation d'agents", ("bon résultat", "?"), ("chemin dangereux", "!"), "juger le voyage, pas seulement la destination", winner="right"),
    "Évaluer un agent sur son comportement, pas seulement son résultat.",
    "Evaluating an agent on its behaviour, not just its result.")
add("taux-hallucination", lambda c: compare(c, "taux d'hallucination", ("modèle seul", "12%"), ("+ RAG sourcé", "2%"), "à exiger sur VOTRE cas d'usage", winner="right"),
    "La proportion de réponses factuellement fausses, réduite par le RAG.",
    "The proportion of factually false answers, reduced by RAG.")
add("test-ab", lambda c: compare(c, "test a/b", ("version A", "50%"), ("version B", "50%"), "mesurer sur le réel bat l'intuition", winner=None),
    "Comparer deux versions auprès d'utilisateurs réels.",
    "Comparing two versions with real users.")
add("regurgitation", lambda c: flow(c, "régurgitation", ["entraînement", "recopie mot à mot", "œuvre protégée"], "un outil créatif, un piège juridique"),
    "Le modèle reproduit mot pour mot des passages de son entraînement.",
    "The model reproduces training passages word for word.")
add("moderation-contenu", lambda c: compare(c, "modération de contenu", ("sur-bloque", "faux +"), ("sous-détecte", "faux −"), "un compromis permanent", winner=None),
    "Filtrer les contenus indésirables à grande échelle, imparfaitement.",
    "Filtering unwanted content at scale, imperfectly.")
add("desinformation-ia", lambda c: hub(c, "désinformation par ia", "FAUX", ["articles", "images", "faux comptes"], "l'échelle change tout"),
    "La production de fausses informations à grande échelle par l'IA.",
    "The large-scale production of false information by AI.")
add("verification-faits", lambda c: flow(c, "vérification des faits", ["affirmation", "recouper sources", "humain décide"], "l'IA assiste, ne remplace pas"),
    "Utiliser l'IA pour aider à vérifier, sans la croire infaillible.",
    "Using AI to help verify, without believing it infallible.")
add("bulle-filtre", lambda c: compare(c, "bulle de filtre", ("personne A", "réalité 1"), ("personne B", "réalité 2"), "plus l'algo vous comprend, plus il vous enferme", winner=None),
    "La personnalisation enferme dans un univers conforme à ses opinions.",
    "Personalisation encloses in a universe conforming to one's opinions.")
add("evaluation-llm", lambda c: flow(c, "évaluation llm", ["jeu de tests", "métriques", "régression bloque"], "systématique, automatisée, intégrée au CI/CD"),
    "Mesurer la qualité d'un LLM par des tests automatisés et humains.",
    "Measuring an LLM's quality through automated and human tests.")
add("monitoring", lambda c: flow(c, "monitoring", ["production", "surveillance", "incident détecté"], "un système non monitoré dérive en silence"),
    "La surveillance continue d'un système d'IA en production.",
    "The continuous monitoring of an AI system in production.")
add("test-validation-ia", lambda c: flow(c, "test & validation ia", ["scénarios tests", "rejeu automatique", "alerte régression"], "protéger sa marque et ses utilisateurs"),
    "Vérifier qu'un système d'IA fonctionne comme attendu.",
    "Verifying that an AI system works as expected.")
