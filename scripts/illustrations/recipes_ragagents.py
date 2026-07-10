# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème RAG & agents."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, points
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("recherche-semantique", lambda c: compare(c, "recherche sémantique", ("mots-clés", "ne trouve pas"), ("par le sens", "trouve"), "le sens l'emporte sur la lettre", winner="right"),
    "Retrouver des documents par le sens, pas par les mots exacts.",
    "Finding documents by meaning, not by exact words.")
add("chunking", lambda c: flow(c, "découpage (chunking)", ["document", "fragments", "vectorisés"], "découper par article, pas à longueur fixe"),
    "Découper les documents en fragments avant de les vectoriser.",
    "Splitting documents into fragments before vectorising them.")
add("chevauchement-fragments", lambda c: beforeafter(c, "chevauchement de fragments", ("clause coupée", "perdue"), ("chevauchement", "lisible"), "un détail aux conséquences concrètes"),
    "Faire se recouvrir les fragments pour ne rien perdre aux frontières.",
    "Overlapping fragments so nothing is lost at boundaries.")
add("recherche-hybride", lambda c: compare(c, "recherche hybride", ("sémantique", "le sens"), ("+ lexicale", "les codes exacts"), "le meilleur des deux mondes", winner=None),
    "Combiner recherche par le sens et par mots-clés exacts.",
    "Combining meaning-based and exact-keyword search.")
add("reclassement", lambda c: beforeafter(c, "reclassement (reranking)", ("50 fragments", "large"), ("5 meilleurs", "précis"), "récupérer large, garder le meilleur"),
    "Réordonner les documents récupérés selon leur pertinence réelle.",
    "Reordering retrieved documents by their real relevance.")
add("top-k", lambda c: meter(c, "top-k", "trop faible", "trop élevé", "plus de contexte peut nuire", pos=0.45),
    "Le nombre de fragments récupérés et fournis au modèle.",
    "The number of fragments retrieved and given to the model.")
add("ancrage", lambda c: compare(c, "ancrage (grounding)", ("de mémoire", "invente"), ("selon ce document", "sourcé"), "la réponse structurelle à l'hallucination", winner="right"),
    "Rattacher les réponses à des sources vérifiables.",
    "Anchoring answers to verifiable sources.")
add("graph-rag", lambda c: hub(c, "graphrag", "GRAPHE", ["entités", "relations", "requête"], "pour les questions relationnelles"),
    "Un RAG s'appuyant sur un graphe de connaissances.",
    "A RAG relying on a knowledge graph.")
add("base-connaissances", lambda c: flow(c, "base de connaissances", ["sources fiables", "RAG", "réponses fiables"], "le vrai cerveau d'un RAG"),
    "L'ensemble structuré des connaissances interrogées par le RAG.",
    "The structured set of knowledge queried by the RAG.")
add("graphe-connaissances", lambda c: hub(c, "graphe de connaissances", "ENTITÉ", ["produit", "client", "fournisseur"], "la rigueur traçable du symbolique"),
    "Des entités reliées par des relations explicites et traçables.",
    "Entities linked by explicit, traceable relations.")
add("appel-fonctions", lambda c: flow(c, "appel de fonctions", ["question", "appel API", "vraie donnée"], "le pont entre le langage et l'action"),
    "Le LLM demande l'exécution de fonctions externes définies.",
    "The LLM requests the execution of defined external functions.")
add("usage-outils", lambda c: hub(c, "usage d'outils", "LLM", ["recherche", "calcul", "code", "base"], "déléguer plutôt que tout savoir"),
    "Utiliser des outils externes pour accomplir des tâches.",
    "Using external tools to accomplish tasks.")
add("mcp", lambda c: hub(c, "model context protocol", "AGENT", ["CRM", "agenda", "docs"], "l'USB de l'IA agentique"),
    "Un protocole ouvert standardisant la connexion des modèles aux outils.",
    "An open protocol standardising models' connection to tools.")
add("protocole-a2a", lambda c: flow(c, "protocole agent à agent", ["agent A", "délègue", "agent B"], "des agents hétérogènes qui coopèrent"),
    "Un protocole permettant à des agents autonomes de se coordonner.",
    "A protocol letting autonomous agents coordinate.")
add("systeme-multi-agents", lambda c: flow(c, "système multi-agents", ["planifie", "recherche", "rédige", "vérifie"], "commencez simple"),
    "Plusieurs agents spécialisés collaborant sur une tâche complexe.",
    "Several specialised agents collaborating on a complex task.")
add("orchestration-ia", lambda c: hub(c, "orchestration ia", "ORCHESTR.", ["petit modèle", "grand modèle", "RAG"], "votre assurance anti-verrouillage"),
    "Coordonner modèles, outils et étapes d'un système d'IA.",
    "Coordinating an AI system's models, tools and steps.")
add("react", lambda c: flow(c, "react · raisonner et agir", ["penser", "agir", "observer"], "un cheminement lisible et auditable", loop=True),
    "L'agent alterne explicitement raisonnement et action.",
    "The agent explicitly alternates reasoning and action.")
add("agent-autonome", lambda c: meter(c, "agent autonome", "supervisé", "autonome", "quel niveau pour quel risque ?", pos=0.6),
    "Un agent poursuivant un objectif sans validation à chaque étape.",
    "An agent pursuing a goal without validation at each step.")
add("controle-ordinateur", lambda c: flow(c, "contrôle d'ordinateur", ["voit l'écran", "clique, saisit", "automatise"], "à réserver aux environnements cloisonnés"),
    "L'agent pilote une interface d'ordinateur comme un humain.",
    "The agent drives a computer interface like a human.")
add("memoire-agent", lambda c: compare(c, "mémoire d'agent", ("continuité", "utile"), ("données perso", "à gouverner"), "le prochain terrain de la vie privée", winner=None),
    "Conserver des informations au-delà d'une seule interaction.",
    "Retaining information beyond a single interaction.")
add("planification-agent", lambda c: flow(c, "planification d'agent", ["objectif", "plan d'étapes", "exécution"], "faire valider le plan avant l'exécution"),
    "Décomposer un objectif complexe en étapes ordonnées.",
    "Breaking a complex goal into ordered steps.")
add("bac-a-sable", lambda c: boundary(c, "bac à sable d'exécution", ["code", "isolé"], "contenir les dégâts d'une erreur", out="sans accès"),
    "Un environnement isolé où le code généré s'exécute sans risque.",
    "An isolated environment where generated code runs safely.")
add("idp", lambda c: flow(c, "traitement intelligent de documents", ["facture", "extraction", "ERP pré-rempli"], "un ROI immédiat sur l'administratif"),
    "Extraire et traiter automatiquement des documents non structurés.",
    "Automatically extracting and processing unstructured documents.")
add("pipeline-ingestion", lambda c: flow(c, "pipeline d'ingestion", ["extraction", "découpage", "indexation"], "tout se joue avant le modèle"),
    "La chaîne préparant les documents pour un RAG.",
    "The chain preparing documents for a RAG.")
add("evaluation-rag", lambda c: compare(c, "évaluation d'un rag", ("récupération", "bons docs ?"), ("génération", "fidèle ?"), "diagnostiquer chaque étage", winner=None),
    "Mesurer séparément la récupération et la génération d'un RAG.",
    "Separately measuring a RAG's retrieval and generation.")
add("ingenierie-contexte", lambda c: flow(c, "ingénierie de contexte", ["instructions", "documents", "l'essentiel, ordonné"], "le vrai savoir-faire de l'IA appliquée"),
    "Composer soigneusement l'information fournie au modèle.",
    "Carefully composing the information provided to the model.")
add("langchain", lambda c: flow(c, "langchain", ["GPT-4", "→ Mistral", "→ local"], "changer de fournisseur sans réécrire"),
    "Une bibliothèque orchestrant LLM, outils et logique métier.",
    "A library orchestrating LLMs, tools and business logic.")
add("langgraph", lambda c: flow(c, "langgraph", ["analyse", "recherche", "validation humaine"], "des flux agentiques contrôlables"),
    "Un framework construisant des applications agentiques en graphes.",
    "A framework building agentic applications as graphs.")
add("flux-agentiques", lambda c: flow(c, "flux agentiques", ["demande", "traiter", "valider", "archiver"], "automatiser des processus, pas des tâches"),
    "Un processus où des agents enchaînent des étapes de bout en bout.",
    "A process where agents chain steps end to end.")
add("similarite-cosinus", lambda c: points(c, "similarité cosinus", "la géométrie n'est pas la compréhension"),
    "Mesurer la proximité de deux vecteurs par l'angle qui les sépare.",
    "Measuring two vectors' proximity by the angle between them.")
add("rag-multimodal", lambda c: hub(c, "rag multimodal", "RAG", ["texte", "schéma", "tableau"], "là où réside le savoir technique"),
    "Un RAG récupérant et raisonnant sur texte, images et schémas.",
    "A RAG retrieving and reasoning over text, images and diagrams.")
add("agents-vocaux", lambda c: flow(c, "agents vocaux", ["écoute", "comprend", "répond"], "annoncer clairement sa nature d'IA"),
    "Des agents IA interagissant par la voix en temps réel.",
    "AI agents interacting by voice in real time.")
add("reformulation-requete", lambda c: beforeafter(c, "reformulation de requête", ('"et pour les CDD ?"', "flou"), ("question complète", "claire"), "rend la conversation naturelle"),
    "Le modèle enrichit la question avant de lancer la recherche.",
    "The model enriches the question before launching the search.")
add("openrag", lambda c: boundary(c, "openrag", ["docs", "internes"], "un RAG souverain, sans SaaS américain", out="rien ne sort"),
    "Une plateforme open source de déploiement RAG souverain.",
    "An open-source sovereign RAG deployment platform.")
