# Liste canonique · lot 3 : complément d'équilibrage des thèmes
# (slug, terme_fr, terme_en, axe, niveau, theme)

TERMES = [
    # ── Données ─────────────────────────────────────────────────────────
    ("exploration-donnees", "Exploration de données (data mining)", "Data mining", "fondamentaux", "fondamental", "donnees"),
    ("caracteristique", "Caractéristique (feature)", "Feature", "fondamentaux", "avance", "donnees"),
    ("extraction-caracteristiques", "Extraction de caractéristiques", "Feature extraction", "fondamentaux", "avance", "donnees"),
    ("reduction-dimension", "Réduction de dimension", "Dimensionality reduction", "fondamentaux", "avance", "donnees"),
    ("echantillonnage", "Échantillon et biais d'échantillonnage", "Sampling and sampling bias", "responsabilite", "intermediaire", "donnees"),
    ("marecage-donnees", "Marécage de données (data swamp)", "Data swamp", "fondamentaux", "avance", "donnees"),
    ("vectorisation", "Vectorisation", "Vectorization", "fondamentaux", "intermediaire", "donnees"),
    ("donnees-dormantes", "Données dormantes (dark data)", "Dark data", "economie", "intermediaire", "donnees"),

    # ── Évaluation & qualité ────────────────────────────────────────────
    ("gpqa", "GPQA", "GPQA", "fondamentaux", "avance", "evaluation-qualite"),
    ("swe-bench", "SWE-bench", "SWE-bench", "fondamentaux", "avance", "evaluation-qualite"),
    ("taux-hallucination", "Taux d'hallucination", "Hallucination rate", "responsabilite", "intermediaire", "evaluation-qualite"),
    ("rouge-bleu", "Métriques ROUGE et BLEU", "ROUGE and BLEU metrics", "fondamentaux", "avance", "evaluation-qualite"),
    ("evaluation-agents", "Évaluation d'agents", "Agent evaluation", "fondamentaux", "avance", "evaluation-qualite"),
    ("moderation-contenu", "Modération de contenu par IA", "AI content moderation", "responsabilite", "intermediaire", "evaluation-qualite"),

    # ── RAG & agents ────────────────────────────────────────────────────
    ("chevauchement-fragments", "Chevauchement de fragments", "Chunk overlap", "fondamentaux", "avance", "rag-agents"),
    ("reformulation-requete", "Reformulation de requête", "Query rewriting", "fondamentaux", "avance", "rag-agents"),
    ("rag-multimodal", "RAG multimodal", "Multimodal RAG", "fondamentaux", "avance", "rag-agents"),
    ("agents-vocaux", "Agents vocaux", "Voice agents", "economie", "intermediaire", "rag-agents"),
    ("langgraph", "LangGraph", "LangGraph", "fondamentaux", "avance", "rag-agents"),
    ("flux-agentiques", "Flux agentiques", "Agentic workflows", "economie", "intermediaire", "rag-agents"),
    ("similarite-cosinus", "Similarité cosinus", "Cosine similarity", "fondamentaux", "avance", "rag-agents"),

    # ── Prompting & usage ───────────────────────────────────────────────
    ("transcription-reunions", "Transcription de réunions par IA", "AI meeting transcription", "economie", "fondamental", "prompting-usage"),
    ("veille-ia", "Veille augmentée par IA", "AI-powered monitoring", "economie", "intermediaire", "prompting-usage"),
    ("fracture-numerique", "Fracture numérique et IA", "AI digital divide", "responsabilite", "fondamental", "prompting-usage"),
    ("ia-accessibilite", "IA et accessibilité", "AI and accessibility", "responsabilite", "intermediaire", "prompting-usage"),

    # ── Impact environnemental ──────────────────────────────────────────
    ("consommation-electrique", "Consommation électrique de l'IA", "AI electricity consumption", "responsabilite", "fondamental", "impact-environnemental"),
    ("empreinte-materielle", "Empreinte matérielle (fabrication)", "Embodied footprint", "responsabilite", "intermediaire", "impact-environnemental"),
    ("neutralite-carbone", "Neutralité carbone des Big Tech", "Big Tech carbon neutrality claims", "responsabilite", "intermediaire", "impact-environnemental"),

    # ── Sécurité ────────────────────────────────────────────────────────
    ("fraude-ia", "Fraude augmentée par IA", "AI-enabled fraud", "responsabilite", "fondamental", "securite"),
    ("classification-information", "Classification de l'information", "Data classification", "economie", "intermediaire", "securite"),

    # ── Entraînement & apprentissage ────────────────────────────────────
    ("dropout", "Abandon (dropout)", "Dropout", "fondamentaux", "avance", "entrainement-apprentissage"),

    # ── Architecture & modèles ──────────────────────────────────────────
    ("modeles-multilingues", "Modèles multilingues", "Multilingual models", "souverainete", "intermediaire", "architecture-modeles"),
    ("ia-langue-francaise", "IA et langue française", "AI and the French language", "souverainete", "fondamental", "architecture-modeles"),
    ("tpu", "TPU · Tensor Processing Unit", "TPU (Tensor Processing Unit)", "fondamentaux", "avance", "architecture-modeles"),
    ("modeles-monde", "Modèles du monde", "World models", "fondamentaux", "avance", "architecture-modeles"),

    # ── Écosystème & outils ─────────────────────────────────────────────
    ("kyutai", "Kyutai", "Kyutai (French AI lab)", "souverainete", "avance", "ecosysteme-outils"),
    ("france-2030", "Plan France 2030 et IA", "France 2030 investment plan", "souverainete", "intermediaire", "ecosysteme-outils"),
    ("sommets-ia", "Sommets internationaux sur l'IA", "International AI summits", "reglementaire", "fondamental", "ecosysteme-outils"),
    ("ia-washing", "Écoblanchiment de l'IA (AI washing)", "AI washing", "economie", "intermediaire", "ecosysteme-outils"),

    # ── Cadre juridique ─────────────────────────────────────────────────
    ("surveillance-travail", "Surveillance algorithmique au travail", "Algorithmic workplace surveillance", "reglementaire", "intermediaire", "cadre-juridique"),
    ("signalement-incidents", "Signalement des incidents IA", "AI incident reporting", "reglementaire", "intermediaire", "cadre-juridique"),
    ("decision-automatisee", "Décision entièrement automatisée", "Automated decision-making (GDPR art. 22)", "reglementaire", "intermediaire", "cadre-juridique"),
]
