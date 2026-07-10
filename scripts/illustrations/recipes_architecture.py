# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème architecture & modèles (+ transverses)."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, points, bars
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("intelligence-artificielle", lambda c: hub(c, "intelligence artificielle", "IA", ["percevoir", "raisonner", "apprendre", "créer"], "un champ, pas une chose"),
    "L'ensemble des techniques faisant réaliser aux machines des tâches humaines.",
    "The set of techniques making machines perform human tasks.")
add("apprentissage-automatique", lambda c: beforeafter(c, "apprentissage automatique", ('règles "si... alors"', "vite contournées"), ("apprendre d'exemples", None), "on montre, on ne programme plus"),
    "Les systèmes apprennent à partir de données plutôt que de règles.",
    "Systems learn from data rather than rules.")
add("apprentissage-profond", lambda c: layers(c, "apprentissage profond", [("concepts", POS), ("formes", GOLD), ("contours", INK)], "des couches qui apprennent seules · et opaques"),
    "Des réseaux à nombreuses couches apprenant des représentations abstraites.",
    "Networks with many layers learning abstract representations.")
add("reseau-neurones", lambda c: layers(c, "réseau de neurones", [("sortie", POS), ("couche cachée", INK), ("entrée", INK)], "une structure mathématique, pas un cerveau"),
    "Un modèle de calcul de « neurones » interconnectés en couches.",
    "A computation model of interconnected \"neurons\" in layers.")
add("neurone-artificiel", lambda c: flow(c, "neurone artificiel", ["entrées ×poids", "activation", "sortie"], "la complexité naît du nombre"),
    "L'unité de calcul élémentaire d'un réseau de neurones.",
    "The elementary computation unit of a neural network.")
add("couche-neurones", lambda c: layers(c, "couche de neurones", [("abstraction +", POS), ("motifs", GOLD), ("contours", INK)], "une hiérarchie du simple au complexe"),
    "Un ensemble de neurones traitant l'information au même niveau.",
    "A set of neurons processing information at the same level.")
add("fonction-activation", lambda c: compare(c, "fonction d'activation", ("sans", "relations simples"), ("avec", "relations complexes"), "la non-linéarité change tout", winner="right"),
    "La non-linéarité qui permet d'apprendre des relations complexes.",
    "The non-linearity that allows learning complex relations.")
add("perceptron", lambda c: flow(c, "perceptron", ["1957", "limite : 1969", "hiver de l'IA"], "l'échec d'une génération, tremplin de la suivante"),
    "Le plus simple des neurones artificiels, aux limites historiques.",
    "The simplest artificial neuron, with historical limits.")
add("algorithme", lambda c: flow(c, "algorithme", ["étape 1", "étape 2", "résultat"], "ni bon ni mauvais en soi"),
    "Une suite finie d'instructions pour résoudre un problème.",
    "A finite sequence of instructions to solve a problem.")
add("parametres", lambda c: compare(c, "paramètres", ("7 milliards", "suffit souvent"), ("1000 milliards", "impressionne"), "résister à la fascination pour la taille", winner="left"),
    "Les valeurs internes qu'un modèle ajuste pour encoder ce qu'il apprend.",
    "The internal values a model adjusts to encode what it learns.")
add("poids-modele", lambda c: flow(c, "poids d'un modèle", ["poids", "exécuter", "adapter"], "qui les détient a la maîtrise"),
    "Les valeurs des paramètres une fois entraîné : tout ce que le modèle « sait ».",
    "The parameter values once trained: all the model \"knows\".")
add("modele-fondation", lambda c: hub(c, "modèle de fondation", "BASE", ["prompt", "RAG", "fine-tuning"], "un point de concentration du pouvoir"),
    "Un grand modèle préentraîné, adapté à de multiples tâches en aval.",
    "A large pre-trained model, adapted to many downstream tasks.")
add("modele-generatif", lambda c: compare(c, "modèle génératif", ('"est-ce un chat ?"', "trie"), ('"dessine un chat"', "crée"), "générer n'est pas anodin", winner="right"),
    "Un modèle produisant du contenu nouveau.",
    "A model producing new content.")
add("modele-discriminatif", lambda c: compare(c, "modèle discriminatif", ("classer, prédire", "sobre"), ("LLM coûteux", "gaspillage"), "le bon type de modèle d'abord", winner="left"),
    "Un modèle qui classe ou prédit, sans générer.",
    "A model that classifies or predicts, without generating.")
add("modele-autoregressif", lambda c: flow(c, "modèle autorégressif", ["mot", "+ mot", "+ mot..."], "le début conditionne toute la suite"),
    "Un modèle générant une séquence élément par élément.",
    "A model generating a sequence element by element.")
add("melange-experts", lambda c: hub(c, "mélange d'experts", "ROUTAGE", ["expert 1", "expert 2", "expert 3"], "n'activer que le nécessaire"),
    "Un grand modèle dont seuls quelques sous-modèles s'activent par requête.",
    "A large model where only a few sub-models activate per request.")
add("gpt", lambda c: layers(c, "g · p · t", [("Génératif", INK), ("Préentraîné", GOLD), ("Transformer", POS)], "trois idées combinées, pas une boîte magique"),
    "Génératif, préentraîné, transformer : trois idées combinées.",
    "Generative, pre-trained, transformer: three combined ideas.")
add("mecanisme-attention", lambda c: hub(c, "mécanisme d'attention", "MOT", ["mot", "mot", "mot", "mot"], "l'étincelle de la révolution actuelle"),
    "Pondérer dynamiquement l'importance des éléments d'une séquence.",
    "Dynamically weighing the importance of a sequence's elements.")
add("auto-attention", lambda c: hub(c, "auto-attention", '"il"', ["l'", "avocat", "au", "tribunal"], "coût quadratique avec la longueur"),
    "Chaque élément est mis en relation avec tous les autres.",
    "Each element is related to all the others.")
add("fenetre-contextuelle", lambda c: meter(c, "fenêtre contextuelle", "8k tokens", "2M tokens", "un RAG bien chunké bat un prompt géant", pos=0.6),
    "Le volume maximal de texte traité en une seule fois.",
    "The maximum volume of text processed at once.")
add("inference", lambda c: compare(c, "inférence", ("entraînement", "1 fois"), ("inférence", "×millions"), "90% des coûts sur 3 ans", winner=None),
    "La phase d'utilisation d'un modèle déjà entraîné.",
    "The phase of using an already-trained model.")
add("temperature", lambda c: meter(c, "température", "0 · factuel", "1 · créatif", "température basse pour la conformité", pos=0.25),
    "Le paramètre contrôlant l'aléa des sorties d'un modèle.",
    "The parameter controlling the randomness of a model's outputs.")
add("top-p", lambda c: meter(c, "top-p", "prévisible", "varié", "brider la diversité réduit les hallucinations", pos=0.4),
    "Le paramètre contrôlant la diversité des sorties.",
    "The parameter controlling output diversity.")
add("logits", lambda c: flow(c, "logits", ["scores bruts", "→ probabilités", "tirage"], "ni intention ni volonté, des scores"),
    "Les scores bruts d'un modèle avant conversion en probabilités.",
    "A model's raw scores before conversion into probabilities.")
add("modele-raisonnement", lambda c: compare(c, "modèle de raisonnement", ("problème dur", "excelle"), ("résumer un email", "gaspillage"), "réfléchir plus quand il le faut", winner="left"),
    "Des modèles entraînés à réfléchir avant de répondre.",
    "Models trained to think before answering.")
add("capacites-emergentes", lambda c: beforeafter(c, "capacités émergentes", ("petit modèle", "échoue"), ("grand modèle", "capacité surgit"), "aussi des comportements indésirables"),
    "Des aptitudes apparaissant brusquement à partir d'une certaine taille.",
    "Abilities appearing abruptly beyond a certain size.")
add("lois-echelle", lambda c: compare(c, "lois d'échelle", ("plus gros", "meilleur"), ("rendements", "décroissants"), "l'efficience plutôt que la taille brute", winner=None),
    "La performance s'améliore avec la taille, mais à rendements décroissants.",
    "Performance improves with size, but with diminishing returns.")
add("agi", lambda c: compare(c, "ia générale (agi)", ("code brillant", "puissant"), ("bon sens physique", "échoue"), "concept marketing autant qu'hypothèse", winner=None),
    "Une hypothétique IA égalant l'intelligence humaine partout.",
    "A hypothetical AI matching human intelligence everywhere.")
add("ia-faible-forte", lambda c: compare(c, "ia faible / forte", ("toutes nos IA", "faibles"), ("IA forte", "hypothétique"), "un outil, pas un être qui pense", winner="left"),
    "Toutes les IA existantes sont « faibles » et spécialisées.",
    "All existing AIs are \"narrow\" and specialised.")
add("superintelligence", lambda c: compare(c, "superintelligence", ("imminente ?", "?"), ("spéculative ?", "?"), "les risques présents méritent autant d'attention", winner=None),
    "Une hypothétique IA dépassant très largement l'humain.",
    "A hypothetical AI vastly exceeding humans.")
add("singularite", lambda c: compare(c, "singularité", ("récit puissant", "fascine"), ("enjeux présents", "détourne"), "le présent mérite plus que la prophétie", winner="right"),
    "L'hypothèse d'une explosion d'intelligence échappant au contrôle.",
    "The hypothesis of an intelligence explosion escaping control.")
add("test-turing", lambda c: compare(c, "test de turing", ("imite la conversation", "franchi"), ("pense ?", "non"), "l'apparence n'est pas l'essence", winner=None),
    "Une machine réussit si on ne peut la distinguer d'un humain.",
    "A machine passes if it cannot be distinguished from a human.")
add("hiver-ia", lambda c: bars(c, "hivers de l'ia", [("emballement", 0.9, INK), ("désillusion", 0.2, DIM)], "l'IA a déjà connu ces cycles"),
    "Des périodes où les promesses non tenues ont tari les financements.",
    "Periods where unmet promises dried up funding.")
add("systeme-expert", lambda c: compare(c, "système expert", ("réseau neurones", "boîte noire"), ("règles explicites", "boîte de verre"), "la transparence totale", winner="right"),
    "Un programme reproduisant un raisonnement d'expert par règles.",
    "A program reproducing expert reasoning through rules.")
add("modeles-symboliques", lambda c: compare(c, "ia symbolique", ("statistique", "corrèle"), ("règles logiques", "traçable"), "le neuro-symbolique, une synthèse", winner=None),
    "L'IA fondée sur des règles et un raisonnement logique explicite.",
    "AI based on explicit rules and logical reasoning.")
add("ontologie", lambda c: hub(c, "ontologie", "CONCEPTS", ["molécule", "maladie", "traitement"], "la rigueur du symbolique"),
    "Une représentation formelle des concepts d'un domaine.",
    "A formal representation of a domain's concepts.")
add("web-semantique", lambda c: flow(c, "web sémantique", ["données liées", "structuré", "interrogeable"], "ce qui manque aux LLM"),
    "Un web où l'information est structurée pour les machines.",
    "A web where information is structured for machines.")
add("ia-generative-note", lambda c: None, "", "")  # placeholder, removed below
del R["ia-generative-note"]

add("ia-non-generative", lambda c: compare(c, "ia non générative", ("classer, prédire", "sobre"), ("génératif partout", "pression"), "80% des problèmes se résolvent mieux ainsi", winner="left"),
    "Les systèmes qui prédisent ou classifient sans générer.",
    "Systems that predict or classify without generating.")
add("gpu", lambda c: compare(c, "gpu", ("NVIDIA", "quasi-monopole"), ("Europe", "dépendante"), "la souveraineté commence dans le silicium", winner=None),
    "Le processeur graphique devenu indispensable à l'IA.",
    "The graphics processor become essential to AI.")
add("tpu", lambda c: compare(c, "tpu", ("Google", "ses propres puces"), ("dépendance", "réduite"), "concevoir ses puces, un avantage", winner="left"),
    "Un processeur conçu par Google pour accélérer l'IA.",
    "A processor designed by Google to accelerate AI.")
add("cache-kv", lambda c: flow(c, "cache clés-valeurs", ["génération", "mémorise", "accélère"], "les longs contextes gonflent la mémoire"),
    "Un cache accélérant l'inférence, coûteux en mémoire sur longs contextes.",
    "A cache speeding inference, memory-costly on long contexts.")
add("decodage-speculatif", lambda c: flow(c, "décodage spéculatif", ["petit modèle propose", "grand vérifie", "plus rapide"], "gagner par l'ingéniosité, pas la force brute"),
    "Un petit modèle propose, le grand valide plusieurs tokens d'un coup.",
    "A small model proposes, the large validates several tokens at once.")
add("traitement-par-lots", lambda c: beforeafter(c, "traitement par lots", ("une à une", None), ("groupées", "débit ×"), "mieux utiliser le matériel qu'on a"),
    "Regrouper les requêtes pour optimiser l'usage du matériel.",
    "Grouping requests to optimise hardware use.")
add("quantification", lambda c: beforeafter(c, "quantification", ("16 bits", "lourd"), ("4 bits", "léger"), "de grands modèles sur du matériel modeste"),
    "Réduire la précision des paramètres pour alléger un modèle.",
    "Reducing parameter precision to lighten a model.")
add("elagage", lambda c: beforeafter(c, "élagage", ("modèle dense", None), ("superflu retiré", "plus rapide"), "moins mais mieux"),
    "Supprimer les paramètres peu utiles pour alléger le modèle.",
    "Removing low-use parameters to lighten the model.")
add("slm", lambda c: compare(c, "petit modèle (slm)", ("tâches courantes", "suffit"), ("chez vous", "sobre"), "choisir le plus petit qui suffit", winner="left"),
    "Un modèle de taille réduite, sobre et déployable localement.",
    "A reduced-size model, frugal and locally deployable.")
add("inference-locale", lambda c: boundary(c, "inférence locale", ["modèle", "chez vous"], "ce qui ne sort pas ne peut pas fuir", out="hors ligne"),
    "Exécuter un modèle sur son propre matériel, sans cloud.",
    "Running a model on your own hardware, without cloud.")
add("serveur-inference", lambda c: flow(c, "serveur d'inférence", ["requêtes", "vLLM", "débit ×"], "rend la souveraineté opérationnelle"),
    "Un logiciel optimisant l'exécution d'un modèle en production.",
    "Software optimising a model's execution in production.")
add("latence", lambda c: compare(c, "latence", ("modèle lent", "pénible"), ("petit, proche", "fluide"), "le meilleur modèle n'est pas le plus puissant", winner="right"),
    "Le délai entre l'envoi d'une requête et la réponse.",
    "The delay between sending a request and the answer.")
add("edge-computing", lambda c: boundary(c, "informatique en périphérie", ["traiter", "sur place"], "traiter localement ce qui peut l'être", out="pas de cloud"),
    "Traiter les données au plus près de leur source.",
    "Processing data as close as possible to its source.")
add("ia-embarquee", lambda c: boundary(c, "ia embarquée", ["modèle", "dans l'objet"], "faire beaucoup avec peu", out="temps réel"),
    "Une IA intégrée dans un appareil, fonctionnant sans cloud.",
    "AI embedded in a device, working without cloud.")
add("neuromorphique", lambda c: compare(c, "neuromorphique", ("processeur classique", "×1000 conso"), ("puce cerveau", "sobre"), "une piste pour une IA plus sobre", winner="right"),
    "Des puces inspirées du cerveau, très économes en énergie.",
    "Brain-inspired chips, very energy-efficient.")
add("informatique-quantique", lambda c: compare(c, "informatique quantique", ("promesses", "grandes"), ("applications", "rares"), "distinguer l'enthousiasme des faits", winner=None),
    "Un paradigme exploitant la physique quantique, encore expérimental.",
    "A paradigm exploiting quantum physics, still experimental.")
add("model-card", lambda c: layers(c, "notice de modèle", [("capacités", POS), ("limites", GOLD), ("biais connus", INK)], "l'étiquette d'un produit, due à l'utilisateur"),
    "Un document décrivant capacités, limites et biais d'un modèle.",
    "A document describing a model's capabilities, limits and biases.")
add("modeles-monde", lambda c: flow(c, "modèles du monde", ["vidéos", "intuition physique", "anticiper"], "comprendre plutôt que corréler ?"),
    "Des modèles apprenant une représentation du monde physique.",
    "Models learning a representation of the physical world.")
add("modeles-multilingues", lambda c: bars(c, "modèles multilingues", [("anglais", 0.9, INK), ("français", 0.5, POS)], "toutes les langues ne sont pas égales"),
    "Des modèles couvrant plusieurs langues, inégalement.",
    "Models covering several languages, unequally.")
add("ia-langue-francaise", lambda c: compare(c, "ia et langue française", ("+ tokens", "coût caché"), ("Mistral", "réduit l'écart"), "défendre une diversité de visions", winner="right"),
    "La place du français dans l'IA, un enjeu de souveraineté.",
    "French's place in AI, a sovereignty issue.")
add("correlation-causalite", lambda c: compare(c, "corrélation ≠ causalité", ("glaces + noyades", "corrélé"), ("cause : chaleur", "réel"), "l'IA voit la corrélation, pas la cause", winner="right"),
    "L'IA excelle à trouver des corrélations, mais pas la causalité.",
    "AI excels at finding correlations, but not causation.")
add("science-donnees", lambda c: hub(c, "science des données", "MÉTHODE", ["nettoyer", "explorer", "interpréter"], "la rigueur prime sur la technologie"),
    "Extraire connaissance et valeur à partir de données.",
    "Extracting knowledge and value from data.")
add("classification", lambda c: flow(c, "classification", ["email", "modèle léger", "spam / normal"], "le cheval de trait discret de l'IA"),
    "Attribuer une catégorie à une donnée.",
    "Assigning a category to a datum.")
add("regression", lambda c: bars(c, "régression", [("prévision", 0.7, POS)], "prédire un nombre, sobrement"),
    "Prédire une valeur numérique continue.",
    "Predicting a continuous numeric value.")
add("clustering", lambda c: bars(c, "partitionnement (clustering)", [("segment 1", 0.6), ("segment 2", 0.4, POS), ("segment 3", 0.3, GOLD)], "l'humain interprète, l'algo propose"),
    "Regrouper automatiquement des données similaires.",
    "Automatically grouping similar data.")
add("detection-anomalies", lambda c: bars(c, "détection d'anomalies", [("normal", 0.4, DIM), ("normal", 0.42, DIM), ("ANOMALIE", 0.95, INK)], "un ROI tangible, discret"),
    "Repérer les données qui s'écartent significativement de la normale.",
    "Spotting data that deviates significantly from the norm.")
add("systeme-recommandation", lambda c: compare(c, "algorithme de recommandation", ("reflète vos goûts", "?"), ("les façonne", "!"), "conscience de son influence", winner="right"),
    "Suggérer des contenus selon le comportement de l'utilisateur.",
    "Suggesting content based on the user's behaviour.")
add("nlp", lambda c: hub(c, "traitement du langage naturel", "TALN", ["traduire", "résumer", "analyser"], "traiter la forme sans saisir le sens"),
    "Faire traiter et générer le langage humain par des machines.",
    "Having machines process and generate human language.")
add("analyse-sentiments", lambda c: compare(c, "analyse de sentiments", ("tendances de masse", "utile"), ("ironie, contexte", "échappe"), "l'étiquette n'est pas la vérité", winner=None),
    "Déterminer la tonalité émotionnelle d'un texte.",
    "Determining the emotional tone of a text.")
add("reconnaissance-entites", lambda c: flow(c, "reconnaissance d'entités", ["texte", "repérer noms, dates", "structuré"], "une brique discrète au service de la conformité"),
    "Identifier et catégoriser les entités mentionnées dans un texte.",
    "Identifying and categorising entities mentioned in a text.")
add("vision-ordinateur", lambda c: compare(c, "vision par ordinateur", ("contrôle qualité", "inspecter"), ("surveillance", "encadré"), "l'usage fait la frontière", winner=None),
    "Faire analyser des images et vidéos par des machines.",
    "Having machines analyse images and videos.")
add("reconnaissance-parole", lambda c: flow(c, "reconnaissance de la parole", ["voix", "→ texte", "accessibilité"], "l'utilité ne dispense pas du cadre"),
    "Convertir la parole en texte.",
    "Converting speech into text.")
add("synthese-vocale", lambda c: compare(c, "synthèse vocale", ("accessibilité", "utile"), ("clonage", "risque"), "la dualité de l'IA", winner=None),
    "Convertir du texte en parole naturelle.",
    "Converting text into natural speech.")
add("clonage-vocal", lambda c: compare(c, "clonage vocal", ("voix familière", "ne prouve rien"), ("second canal", "vérifier"), "reconnaître une voix ne prouve plus rien", winner="right"),
    "Reproduire la voix d'une personne à partir de quelques secondes.",
    "Reproducing a person's voice from a few seconds.")
add("assistant-vocal", lambda c: compare(c, "assistant vocal", ("service", "réel"), ("écoute permanente", "vie privée"), "qui écoute ?", winner=None),
    "Interagir avec un système par la voix.",
    "Interacting with a system by voice.")
add("ocr", lambda c: flow(c, "reconnaissance de caractères (ocr)", ["image scannée", "→ texte", "exploitable"], "le maillon discret dont tout dépend"),
    "Convertir en texte le contenu d'images ou documents scannés.",
    "Converting scanned images or documents into text.")
add("traduction-automatique", lambda c: compare(c, "traduction automatique", ("courant", "excelle"), ("subtil, culturel", "relire"), "la fluidité ≠ l'exactitude", winner=None),
    "Traduire des textes d'une langue à l'autre par réseaux neuronaux.",
    "Translating texts between languages via neural networks.")
add("multimodal", lambda c: hub(c, "multimodal", "MODÈLE", ["texte", "image", "son"], "une image = milliers de tokens"),
    "Un modèle traitant plusieurs types d'entrées : texte, image, son.",
    "A model processing several input types: text, image, sound.")
add("generation-images", lambda c: flow(c, "génération d'images", ['"un chat..."', "diffusion", "image"], "des œuvres d'artistes en amont"),
    "Produire des images originales à partir d'une description.",
    "Producing original images from a description.")
add("generation-video", lambda c: compare(c, "génération de vidéo", ("créatif", "immense"), ("hypertrucage", "menace"), "un basculement civilisationnel", winner=None),
    "Produire des séquences vidéo réalistes par IA.",
    "Producing realistic video sequences by AI.")
add("generation-audio", lambda c: flow(c, "génération audio", ["description", "IA", "son / musique"], "ce qui libère les uns peut spolier les autres"),
    "Produire sons, voix et musique par IA.",
    "Producing sounds, voices and music by AI.")
add("modeles-diffusion", lambda c: flow(c, "modèles de diffusion", ["bruit", "débruitage", "image"], "très énergivores · droits d'auteur"),
    "Des modèles générant des images en débruitant un bruit aléatoire.",
    "Models generating images by denoising random noise.")
add("gan", lambda c: compare(c, "réseau antagoniste (gan)", ("générateur", "produit"), ("discriminateur", "juge"), "créer et tromper, deux faces d'un pouvoir", winner=None),
    "Deux réseaux s'affrontent pour produire du réel convaincant.",
    "Two networks compete to produce convincing reality.")
add("autoencodeur", lambda c: flow(c, "autoencodeur", ["compresser", "goulot", "reconstruire"], "reconstruire, c'est comprendre"),
    "Un réseau apprenant à compresser puis reconstruire des données.",
    "A network learning to compress then reconstruct data.")
add("espace-latent", lambda c: points(c, "espace latent", "où le sens devient géométrie", query=False),
    "L'espace abstrait où un modèle encode les caractéristiques des données.",
    "The abstract space where a model encodes data features.")
add("encodeur-decodeur", lambda c: flow(c, "encodeur-décodeur", ["comprendre l'entrée", "représentation", "produire la sortie"], "lire puis écrire, deux étapes"),
    "Un encodeur comprend l'entrée, un décodeur produit la sortie.",
    "An encoder understands the input, a decoder produces the output.")
add("reseau-convolutif", lambda c: layers(c, "réseau convolutif (cnn)", [("objets", POS), ("motifs", GOLD), ("contours", INK)], "sobre et spécialisé pour la vision"),
    "Une architecture spécialisée dans le traitement d'images.",
    "An architecture specialised in image processing.")
add("reseau-recurrent", lambda c: compare(c, "réseau récurrent (rnn)", ("longues phrases", "oublie le début"), ("transformer", "résout"), "l'état de l'art d'hier, note de bas de page", winner="right"),
    "Une architecture pour séquences, dépassée par les transformers.",
    "An architecture for sequences, surpassed by transformers.")
add("robotique-ia", lambda c: compare(c, "robotique et ia incarnée", ("manipuler le langage", "brillant"), ("saisir un verre", "difficile"), "l'humilité face au réel", winner=None),
    "L'IA dans des robots percevant et agissant dans le monde.",
    "AI in robots perceiving and acting in the world.")
add("jumeau-numerique", lambda c: flow(c, "jumeau numérique", ["objet réel", "réplique", "simuler"], "expérimenter sans risque sur le réel"),
    "Une réplique numérique d'un système physique, alimentée en données.",
    "A digital replica of a physical system, fed with data.")
add("informatique-affective", lambda c: compare(c, "informatique affective", ("lire les émotions", "douteux"), ("interdite au travail", "encadré"), "une lecture des âmes non validée", winner=None),
    "Prétendre détecter et simuler les émotions humaines.",
    "Claiming to detect and simulate human emotions.")
add("deepfake", lambda c: compare(c, "hypertrucage (deepfake)", ("voir", "≠ croire"), ("provenance", "vérifier"), "la fin de la preuve par la ressemblance", winner="right"),
    "Un contenu où l'IA fabrique le visage ou la voix d'une personne.",
    "Content where AI fabricates a person's face or voice.")
add("chatbot", lambda c: compare(c, "chatbot", ("à règles", "limité"), ("LLM", "souple, hallucine"), "grand public ≠ solution d'entreprise", winner=None),
    "Une interface conversationnelle en langage naturel.",
    "A natural-language conversational interface.")
add("zero-shot-few-shot", lambda c: compare(c, "zero-shot / few-shot", ("zéro exemple", "simple"), ("quelques exemples", "fiable"), "testez le few-shot avant le fine-tuning", winner="right"),
    "Réaliser une tâche sans ou avec quelques exemples, sans réentraînement.",
    "Performing a task with no or a few examples, without retraining.")
