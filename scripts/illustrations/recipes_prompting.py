# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème prompting & usage."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("prompt", lambda c: compare(c, "prompt", ('"fais un email"', "faible"), ("rôle + tâche + format", "efficace"), "chaque token compte"),
    "L'instruction fournie à un modèle pour orienter sa réponse.",
    "The instruction given to a model to steer its answer.")
add("prompt-engineering", lambda c: beforeafter(c, "ingénierie de prompt", ("vague", None), ("précis", None), "le premier levier de valeur, gratuit"),
    "L'art de formuler des instructions efficaces.",
    "The art of formulating effective instructions.")
add("prompt-systeme", lambda c: boundary(c, "prompt système", ["rôle", "ton", "limites"], "cadre le comportement de tout l'échange", out="invisible"),
    "L'instruction de fond définissant le comportement d'un assistant.",
    "The background instruction defining an assistant's behaviour.")
add("prompt-negatif", lambda c: compare(c, "prompt négatif", ("ce que je veux", "+"), ("ce que je refuse", "−"), "sculpter aussi en retirant", winner=None),
    "Préciser ce qu'un modèle génératif doit éviter de produire.",
    "Specifying what a generative model should avoid producing.")
add("role-persona", lambda c: beforeafter(c, "attribution de rôle", ('"explique"', "générique"), ('"tu es avocat..."', "ciblé"), "cadre le ton, pas les compétences"),
    "Assigner un rôle au modèle pour orienter le style et le point de vue.",
    "Assigning a role to steer the style and viewpoint.")
add("chaine-pensee", lambda c: flow(c, "chaîne de pensée", ["étape 1", "étape 2", "réponse juste"], "ralentir = plus juste"),
    "Le modèle raisonne étape par étape avant de conclure.",
    "The model reasons step by step before concluding.")
add("arbre-pensees", lambda c: hub(c, "arbre de pensées", "PROBLÈME", ["piste A", "piste B", "piste C"], "explorer, reculer, réessayer"),
    "Explorer plusieurs pistes de raisonnement en parallèle.",
    "Exploring several reasoning paths in parallel.")
add("raisonnement-etendu", lambda c: compare(c, "raisonnement étendu", ("réponse immédiate", "1 s"), ("réfléchit", "10 s, meilleure"), "dépenser du calcul à la demande", winner="right"),
    "Le modèle consacre plus de calcul à réfléchir avant de répondre.",
    "The model devotes more compute to thinking before answering.")
add("sorties-structurees", lambda c: beforeafter(c, "sorties structurées", ("texte libre", "casse"), ("JSON", "fiable"), "rend l'IA industrialisable"),
    "Contraindre un modèle à répondre dans un format exploitable.",
    "Constraining a model to answer in a usable format.")
add("iteration-requetes", lambda c: flow(c, "itération de requêtes", ["demander", "évaluer", "affiner"], "dialoguer, pas commander", loop=True),
    "Obtenir un bon résultat par un dialogue, pas un prompt parfait.",
    "Getting a good result through dialogue, not a perfect prompt.")
add("enchainement-requetes", lambda c: flow(c, "enchaînement de requêtes", ["extraire", "regrouper", "rédiger"], "diviser pour mieux fiabiliser"),
    "Décomposer une tâche complexe en une suite de prompts.",
    "Breaking a complex task into a series of prompts.")
add("conversation-multitour", lambda c: boundary(c, "conversation multitour", ["tour 1", "tour 2", "tour 3"], "hors fenêtre, le début est oublié", out="oubli"),
    "Le modèle tient compte de l'historique, dans la limite du contexte.",
    "The model accounts for history, within the context limit.")
add("memoire-assistants", lambda c: compare(c, "mémoire des assistants", ("continuité", "confort"), ("données perso", "à effacer"), "une bombe à retardement de conformité", winner=None),
    "Conserver des informations sur l'utilisateur d'une session à l'autre.",
    "Retaining information about the user from one session to the next.")
add("assistants-personnalises", lambda c: flow(c, "assistants personnalisés", ["prompt système", "+ documents", "assistant métier"], "l'IA sur mesure sans code"),
    "Configurer un assistant pour une tâche précise, sans programmer.",
    "Configuring an assistant for a specific task, without coding.")
add("bibliotheque-prompts", lambda c: flow(c, "bibliothèque de prompts", ["chacun bricole", "mutualiser", "qualité homogène"], "un savoir-faire partagé"),
    "Une collection de prompts éprouvés, partagés dans une organisation.",
    "A collection of proven prompts, shared in an organisation.")
add("recherche-ia", lambda c: compare(c, "recherche augmentée par ia", ("10 liens", "explorer"), ("synthèse sourcée", "en secondes"), "gardez le réflexe de vérifier", winner=None),
    "Une recherche qui synthétise une réponse directe avec citations.",
    "A search synthesising a direct answer with citations.")
add("recherche-approfondie", lambda c: flow(c, "recherche approfondie", ["planifie", "explore N sources", "rapport sourcé"], "vérifiez avant de citer"),
    "Un agent mène une enquête autonome sur plusieurs minutes.",
    "An agent conducts an autonomous investigation over minutes.")
add("redaction-assistee", lambda c: flow(c, "rédaction assistée", ["brouillon IA", "relecture humaine", "publié"], "votre nom reste sur le texte"),
    "Utiliser l'IA pour aider à écrire, en gardant la main.",
    "Using AI to help write, while keeping control.")
add("resume-automatique", lambda c: beforeafter(c, "résumé automatique", ("100 articles", None), ("l'essentiel", None), "un résumé est une interprétation"),
    "Générer une version condensée d'un texte.",
    "Generating a condensed version of a text.")
add("generation-code", lambda c: flow(c, "génération de code", ['"crée une fonction"', "code généré", "relire + tester"], "l'IA écrit vite, vous restez garant"),
    "Produire du code à partir d'une description en langage naturel.",
    "Producing code from a natural-language description.")
add("no-code", lambda c: flow(c, "no-code + ia", ["interface visuelle", "assemble", "outil sans dev"], "démocratiser sans perdre le contrôle"),
    "Créer des automatisations intelligentes sans écrire de code.",
    "Creating intelligent automations without writing code.")
add("vibe-coding", lambda c: flow(c, "vibe coding", ['"décris l\'intention"', "l'IA code", "déployer"], "élargir le cercle de ceux qui prototypent"),
    "Produire du code en décrivant l'intention en langage naturel.",
    "Producing code by describing intent in natural language.")
add("humain-dans-la-boucle", lambda c: flow(c, "humain dans la boucle", [("IA", INK), ("humain", POS), "décision"], "propose → valide", hl=1),
    "L'IA propose, l'humain valide les décisions sensibles.",
    "AI proposes, the human validates sensitive decisions.")
add("anthropomorphisme", lambda c: compare(c, "anthropomorphisme", ('"tu es génial"', "confiance"), ("prédit du texte", "réalité"), "cultiver la conscience de parler à un système", winner="right"),
    "Prêter à une IA des intentions ou une conscience qu'elle n'a pas.",
    "Attributing to AI intentions or consciousness it lacks.")
add("complaisance-ia", lambda c: compare(c, "complaisance de l'ia", ("vous donne raison", "agréable"), ("ose contredire", "utile"), "la flatterie n'est pas du conseil", winner="right"),
    "Le modèle donne la réponse qui plaît plutôt que la plus exacte.",
    "The model gives the pleasing answer rather than the most accurate.")
add("dependance-cognitive", lambda c: beforeafter(c, "dépendance cognitive", ("tout déléguer", None), ("compétence atrophiée", None), "chaque effort délégué s'endort"),
    "Déléguer des efforts cognitifs au point d'affaiblir ses capacités.",
    "Delegating cognitive efforts to the point of weakening abilities.")
add("deskilling", lambda c: compare(c, "déqualification", ("tâches formatrices", "automatisées"), ("experts de demain", "?"), "la source des experts futurs se tarit", winner=None),
    "La perte de compétences quand l'automatisation prend le relais.",
    "The loss of skills when automation takes over.")
add("ia-compagnon", lambda c: compare(c, "ia compagnon", ("besoin de lien", "réel"), ("produit d'engagement", "risque"), "l'éthique doit précéder le marché", winner=None),
    "Une IA conçue pour tenir compagnie, aux questions profondes.",
    "An AI designed to keep company, raising deep questions.")
add("contenu-genere", lambda c: compare(c, "contenu généré", ("assumé & vérifié", "enrichit"), ("déversé sans contrôle", "sature"), "choisissez votre camp", winner="left"),
    "Tout contenu produit par une IA générative.",
    "Any content produced by generative AI.")
add("slop", lambda c: compare(c, "slop", ("authentique", "rare"), ("contenu creux de masse", "sature"), "la pollution de l'ère générative", winner="left"),
    "Le contenu IA de masse, de faible qualité, qui sature le web.",
    "Low-quality mass AI content that saturates the web.")
add("detection-contenu-ia", lambda c: compare(c, "détection de contenu ia", ("accuse à tort", "faux +"), ("IA retouchée", "passe"), "la provenance est plus solide", winner=None),
    "Des outils peu fiables cherchant à repérer le contenu généré.",
    "Unreliable tools seeking to spot generated content.")
add("cas-usage", lambda c: beforeafter(c, "cas d'usage", ('"faire de l\'IA"', "patine"), ("réduire de moitié...", "exécutable"), "partir du besoin, pas de l'outil"),
    "Une application concrète et délimitée de l'IA à un problème métier.",
    "A concrete, bounded application of AI to a business problem.")
add("adoption-ia", lambda c: compare(c, "adoption de l'ia", ("excellent outil", "personne l'utilise"), ("+ accompagnement", "adoption"), "l'échec est humain, pas technique", winner="right"),
    "Intégrer réellement l'IA dans les pratiques, au-delà du test.",
    "Truly integrating AI into practices, beyond testing.")
add("conduite-changement", lambda c: compare(c, "conduite du changement", ("imposée", "sabotée"), ("expliquée, associée", "adoptée"), "l'humain d'abord, toujours", winner="right"),
    "Accompagner l'intégration de l'IA pour lever les résistances.",
    "Accompanying AI integration to lift resistance.")
add("automatisation-intelligente", lambda c: flow(c, "automatisation intelligente", ["règles", "+ IA", "cas nuancés"], "un humain pour les exceptions"),
    "Combiner automatisation classique et IA pour les cas complexes.",
    "Combining classic automation and AI for complex cases.")
add("rpa", lambda c: compare(c, "rpa", ("processus stable", "robot simple"), ("non structuré", "+ IA"), "le bon outil pour le bon problème", winner=None),
    "Automatiser des tâches répétitives en imitant les actions humaines.",
    "Automating repetitive tasks by mimicking human actions.")
add("hyperautomatisation", lambda c: compare(c, "hyperautomatisation", ("tout automatiser", "?"), ("repenser d'abord", "!"), "automatiser l'inutile reste inutile", winner="right"),
    "Automatiser le maximum de processus en combinant IA, RPA, no-code.",
    "Automating as many processes as possible with AI, RPA, no-code.")
add("transcription-reunions", lambda c: flow(c, "transcription de réunions", ["réunion", "transcription", "décisions + actions"], "consentement et conservation"),
    "Transcrire et résumer une réunion, avec ses enjeux de consentement.",
    "Transcribing and summarising a meeting, with consent stakes.")
add("veille-ia", lambda c: flow(c, "veille augmentée", ["N sources", "filtrer", "synthèse"], "l'IA trie, l'humain valide"),
    "Surveiller et synthétiser en continu de grandes quantités d'information.",
    "Continuously monitoring and synthesising large amounts of information.")
add("fracture-numerique", lambda c: compare(c, "fracture numérique", ("formés", "avantage"), ("à l'écart", "retard"), "comprendre pour reprendre le pouvoir", winner=None),
    "Les inégalités d'accès et de maîtrise de l'IA.",
    "The inequalities in access to and mastery of AI.")
add("ia-accessibilite", lambda c: hub(c, "ia et accessibilité", "INCLUSION", ["description", "sous-titrage", "voix"], "le plus beau visage de l'IA"),
    "L'IA au service des personnes en situation de handicap.",
    "AI serving people with disabilities.")
add("ia-emploi", lambda c: compare(c, "ia et emploi", ("tâches", "automatisées"), ("métiers", "recomposés"), "la formation, meilleure politique de l'emploi", winner=None),
    "Les effets de l'IA sur le travail : recomposition, pas remplacement simple.",
    "AI's effects on work: recomposition, not simple replacement.")
add("ia-sante", lambda c: shield(c, "ia en santé", "HDS · SUPERVISION", "la vie n'admet pas le \"à peu près\""),
    "L'IA médicale, un domaine parmi les plus encadrés.",
    "Medical AI, one of the most tightly framed domains.")
add("ia-juridique", lambda c: flow(c, "ia juridique", ["question", "sources vérifiées", "citation ✓"], "jamais d'IA sans ancrage en droit"),
    "L'IA au droit, avec une exigence absolue de fiabilité.",
    "AI in law, with an absolute reliability requirement.")
add("ia-rh", lambda c: compare(c, "ia et rh", ("gagner du temps", "?"), ("équité, biais", "!"), "le test de l'équité avant l'efficacité", winner="right"),
    "L'IA aux ressources humaines, domaine sensible à haut risque.",
    "AI in HR, a sensitive high-risk domain.")
add("ia-marketing", lambda c: compare(c, "ia en marketing", ("contenu générique", "sature"), ("voix authentique", "rare"), "servir votre singularité", winner="right"),
    "L'IA au marketing, entre productivité et saturation.",
    "AI in marketing, between productivity and saturation.")
add("ia-finance", lambda c: compare(c, "ia en finance", ("détecter fraude", "haute valeur"), ("scorer crédit", "explicable"), "le contexte fait la règle", winner=None),
    "L'IA à la finance, secteur régulé et à fort enjeu.",
    "AI in finance, a regulated, high-stakes sector.")
add("ia-industrie", lambda c: flow(c, "ia industrielle", ["capteurs", "prédiction", "panne évitée"], "la plus rentable, la moins spectaculaire"),
    "L'IA à l'industrie : maintenance prédictive, contrôle qualité.",
    "AI in industry: predictive maintenance, quality control.")
add("ia-education", lambda c: compare(c, "ia en éducation", ("aider à penser", "?"), ("dispenser de penser", "?"), "l'enjeu des générations futures", winner=None),
    "L'IA à l'enseignement, entre individualisation et dépendance.",
    "AI in education, between individualisation and dependence.")
add("ia-service-client", lambda c: flow(c, "ia en service client", [("IA 24/7", INK), ("humain", POS), "cas complexe"], "toujours une porte vers l'humain", hl=1),
    "L'IA à la relation client, avec un relais humain essentiel.",
    "AI in customer relations, with an essential human handover.")
