# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème écosystème & outils."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter, brand, bars
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

# Acteurs (cartes de marque)
add("openai", lambda c: brand(c, "OpenAI", "domination US · dépendance à peser", "ChatGPT · GPT"),
    "L'entreprise américaine créatrice de ChatGPT et des modèles GPT.",
    "The American company that created ChatGPT and the GPT models.")
add("anthropic", lambda c: brand(c, "Anthropic", "sûreté · reste hébergé aux US", "Claude"),
    "L'entreprise américaine créatrice de Claude, axée sur la sûreté.",
    "The American company that created Claude, focused on safety.")
add("google-deepmind", lambda c: brand(c, "DeepMind", "AlphaFold · pouvoir des géants", "Gemini"),
    "La division IA de Google, puissante en recherche.",
    "Google's AI division, powerful in research.")
add("meta-ai", lambda c: brand(c, "Meta AI", "poids ouverts · sert l'écosystème", "LLaMA"),
    "La division IA de Meta, créatrice de LLaMA en poids ouverts.",
    "Meta's AI division, creator of open-weights LLaMA.")
add("nvidia", lambda c: brand(c, "NVIDIA", "quasi-monopole · point de fragilité", "GPU"),
    "L'entreprise dominant le marché des GPU indispensables à l'IA.",
    "The company dominating the market for AI-essential GPUs.")
add("le-chat", lambda c: brand(c, "Le Chat", "alternative européenne à ChatGPT", "Mistral"),
    "L'assistant conversationnel français de Mistral AI.",
    "Mistral AI's French conversational assistant.")
add("grok", lambda c: brand(c, "Grok", "moins bridé · quels garde-fous ?", "xAI"),
    "L'assistant de xAI, intégré au réseau X.",
    "xAI's assistant, integrated into the X network.")
add("deepseek", lambda c: brand(c, "DeepSeek", "Chine · poids ouverts à bas coût", "open weights"),
    "L'entreprise chinoise publiant des modèles ouverts à bas coût.",
    "The Chinese company releasing low-cost open models.")
add("qwen", lambda c: brand(c, "Qwen", "Alibaba · fort en multilingue", "open weights"),
    "La famille de modèles ouverts d'Alibaba, forte en multilingue.",
    "Alibaba's open-model family, strong in multilingual tasks.")
add("mistral-ai", lambda c: brand(c, "Mistral AI", "modèles ouverts · France", "souverain"),
    "L'acteur français des modèles ouverts, alternative souveraine.",
    "The French open-model player, a sovereign alternative.")
add("chatgpt", lambda c: brand(c, "ChatGPT", "grand public ≠ entreprise", "OpenAI"),
    "L'application qui a popularisé les LLM auprès du grand public.",
    "The app that brought LLMs to the general public.")
add("claude", lambda c: brand(c, "Claude", "fenêtre 200k · Constitutional AI", "Anthropic"),
    "La famille de modèles d'Anthropic, méthode Constitutional AI.",
    "Anthropic's model family, Constitutional AI method.")
add("gemini", lambda c: brand(c, "Gemini", "fenêtre géante · Workspace", "Google"),
    "Les modèles multimodaux de Google, intégrés à Workspace.",
    "Google's multimodal models, integrated into Workspace.")
add("llama", lambda c: brand(c, "LLaMA", "poids ouverts · licence à lire", "Meta"),
    "La famille de modèles à poids ouverts de Meta.",
    "Meta's open-weights model family.")
add("copilot", lambda c: brand(c, "Copilot", "puissant · porte ouverte sur vos données", "Microsoft 365"),
    "L'assistant IA intégré à la suite Microsoft 365.",
    "The AI assistant built into Microsoft 365.")
add("hugging-face", lambda c: brand(c, "Hugging Face", "1M+ modèles · pilier open source", "plateforme"),
    "La plus grande plateforme open source de modèles et datasets.",
    "The largest open-source platform for models and datasets.")
add("albert", lambda c: brand(c, "Albert", "l'IA souveraine de l'État français", "DINUM"),
    "La suite d'IA générative de l'administration française.",
    "The French administration's generative AI suite.")
add("kyutai", lambda c: brand(c, "Kyutai", "recherche ouverte · vocal temps réel", "France"),
    "Un laboratoire français de recherche ouverte en IA.",
    "A French open AI research lab.")
add("bloom", lambda c: brand(c, "BLOOM", "ouvert · transparent · collaboratif", "BigScience"),
    "Un grand modèle ouvert issu d'une collaboration internationale.",
    "A large open model from an international collaboration.")
add("cursor", lambda c: brand(c, "Cursor", "IDE IA · restez garant du code", "dev"),
    "Un IDE intégrant profondément l'IA pour assister les développeurs.",
    "An IDE deeply integrating AI to assist developers.")
add("github-copilot", lambda c: brand(c, "GitHub Copilot", "pionnier · licences du code appris", "code"),
    "L'assistant de programmation de GitHub et OpenAI.",
    "GitHub and OpenAI's programming assistant.")
add("perplexity", lambda c: brand(c, "Perplexity", "recherche générative · vérifiez", "search"),
    "Un moteur de recherche augmenté par IA avec citations.",
    "An AI-augmented search engine with citations.")
add("notebooklm", lambda c: brand(c, "NotebookLM", "RAG grand public · docs chez Google", "Google"),
    "L'outil de Google pour dialoguer avec ses propres documents.",
    "Google's tool to dialogue with your own documents.")
add("sora", lambda c: brand(c, "Sora", "vidéo générative · provenance urgente", "OpenAI"),
    "Le modèle de génération de vidéo d'OpenAI.",
    "OpenAI's video generation model.")
add("midjourney", lambda c: brand(c, "Midjourney", "esthétique · droits à vérifier", "images"),
    "Un service de génération d'images à forte qualité esthétique.",
    "An image generation service with high aesthetic quality.")
add("stable-diffusion", lambda c: brand(c, "Stable Diffusion", "poids ouverts · local & personnalisable", "images"),
    "Un modèle de génération d'images à poids ouverts, exécutable en local.",
    "An open-weights image generation model, runnable locally.")
add("ovhcloud", lambda c: brand(c, "OVHcloud", "cloud souverain · SecNumCloud, HDS", "France"),
    "Le principal fournisseur de cloud souverain européen.",
    "The leading European sovereign cloud provider.")
add("scaleway", lambda c: brand(c, "Scaleway", "cloud GPU souverain · Iliad", "France"),
    "Un fournisseur de cloud français, offres GPU pour l'IA.",
    "A French cloud provider with GPU offers for AI.")
add("ollama", lambda c: brand(c, "Ollama", "inférence locale · données privées", "open source"),
    "Un outil pour exécuter facilement des modèles ouverts en local.",
    "A tool to easily run open models locally.")
add("open-webui", lambda c: brand(c, "OpenWebUI", "un ChatGPT privé et souverain", "open source"),
    "Une interface web pour un assistant privé au-dessus de modèles locaux.",
    "A web interface for a private assistant over local models.")
add("vllm", lambda c: brand(c, "vLLM", "inférence performante · souveraine", "open source"),
    "Une bibliothèque d'inférence haute performance pour LLM.",
    "A high-performance inference library for LLMs.")
add("litellm", lambda c: brand(c, "LiteLLM", "interface unifiée · zéro lock-in", "open source"),
    "Une interface unifiée pour appeler des dizaines de fournisseurs.",
    "A unified interface to call dozens of providers.")
add("pytorch", lambda c: brand(c, "PyTorch", "commun open source de l'IA moderne", "Meta"),
    "La bibliothèque de référence pour développer des modèles.",
    "The reference library for developing models.")

# Concepts d'écosystème
add("mlops", lambda c: flow(c, "mlops", ["entraîner", "déployer", "surveiller"], "un modèle est un système vivant", loop=True),
    "Industrialiser le cycle de vie des modèles de machine learning.",
    "Industrialising the machine learning model lifecycle.")
add("llmops", lambda c: flow(c, "llmops", ["prompts", "évaluation", "coûts & hallucinations"], "piloter par la donnée, pas l'intuition"),
    "Le MLOps spécifique aux grands modèles de langage.",
    "MLOps specific to large language models.")
add("aiaas", lambda c: compare(c, "ia en tant que service", ("louer l'API", "rapide"), ("posséder l'infra", "maîtrise"), "facilité immédiate vs souveraineté", winner=None),
    "L'IA fournie à la demande via le cloud, sous forme d'API.",
    "AI provided on demand via the cloud, as APIs.")
add("tarification-usage", lambda c: compare(c, "tarification à l'usage", ("petits volumes", "modeste"), ("à l'échelle", "explose"), "simulez votre TCO sur 3 ans", winner=None),
    "La facturation des API au prorata des tokens traités.",
    "Billing APIs in proportion to tokens processed.")
add("gpu-cloud", lambda c: brand(c, "Cloud GPU", "louer la puissance · choisir souverain", "à la demande"),
    "L'accès à la demande à des GPU puissants sans acheter le matériel.",
    "On-demand access to powerful GPUs without buying hardware.")
add("build-vs-buy", lambda c: compare(c, "développer ou acheter", ("acheter", "dépendance"), ("développer", "maîtrise"), "assez stratégique pour le maîtriser ?", winner=None),
    "L'arbitrage entre développer en interne et acheter du marché.",
    "The trade-off between building in-house and buying.")
add("roi-ia", lambda c: compare(c, "roi de l'ia", ("10 projets", "sans mesure"), ("3 projets", "suivis"), "ce qui ne se mesure pas ne se pilote pas", winner="right"),
    "Mesurer la valeur réelle créée face au coût total.",
    "Measuring the real value created against the total cost.")
add("poc", lambda c: compare(c, "preuve de concept", ("POC brillant", "démo"), ("passage à l'échelle", "?"), "pensez production dès le pilote", winner=None),
    "Un pilote démontrant la faisabilité avant tout déploiement.",
    "A pilot demonstrating feasibility before deployment.")
add("freemium", lambda c: compare(c, "gratuit-payant", ("gratuit", "vos données"), ("payant", "précaution"), "si c'est gratuit, vous êtes le produit", winner="right"),
    "Un service gratuit dont l'utilisateur « paie » souvent avec ses données.",
    "A free service where the user often \"pays\" with their data.")
add("bulle-ia", lambda c: compare(c, "bulle spéculative", ("valorisations", "×"), ("revenus réels", "?"), "raisonner par la valeur, pas la mode", winner=None),
    "La crainte d'une survalorisation financière de l'IA.",
    "The fear of a financial overvaluation of AI.")
add("ia-washing", lambda c: compare(c, "ia-washing", ('"propulsé par l\'IA"', "vernis"), ("règles simples", "réalité"), "exigez du concret", winner="right"),
    "Exagérer ou inventer l'usage de l'IA dans un produit.",
    "Exaggerating or inventing the use of AI in a product.")
add("course-ia", lambda c: compare(c, "course mondiale à l'ia", ("vitesse", "US, Chine"), ("responsabilité", "Europe"), "une course différente, pas perdue", winner="right"),
    "La compétition entre puissances pour dominer l'IA.",
    "The competition between powers to dominate AI.")
add("chief-ai-officer", lambda c: hub(c, "chief ai officer", "CAIO", ["vision", "gouvernance", "priorités"], "le mandat, pas seulement le titre"),
    "La fonction pilotant la stratégie IA au plus haut niveau.",
    "The role steering AI strategy at the top level.")
add("metiers-ia", lambda c: hub(c, "nouveaux métiers de l'ia", "COMPÉTENCES", ["data sci.", "prompt eng.", "éthicien"], "les profils hybrides sont recherchés"),
    "Les professions nées ou transformées par l'IA.",
    "The professions born or transformed by AI.")
add("licences-open-source", lambda c: compare(c, "licences open source", ("Apache/MIT", "tout usage"), ("restrictive", "à lire"), "\"open\" ≠ libre de tout usage", winner="left"),
    "Les cadres juridiques régissant l'usage des modèles ouverts.",
    "The legal frameworks governing open-model use.")
add("autonomie-strategique", lambda c: hub(c, "autonomie stratégique", "EUROPE", ["infra", "modèles", "puces", "données"], "l'assurance-vie géopolitique"),
    "La capacité de l'Europe à décider par elle-même dans le numérique.",
    "Europe's ability to decide for itself in digital matters.")
add("chips-act", lambda c: flow(c, "chips act européen", ["dépendance puces", "usines EU", "souveraineté"], "la souveraineté commence dans le silicium"),
    "Le règlement renforçant la production de puces en Europe.",
    "The regulation strengthening chip production in Europe.")
add("euro-stack", lambda c: layers(c, "eurostack", [("applications", POS), ("modèles", POS), ("cloud", GOLD), ("puces", INK)], "la souveraineté est un système"),
    "La vision d'une pile technologique européenne complète.",
    "The vision of a complete European technology stack.")
add("gaia-x", lambda c: compare(c, "gaia-x", ("labels", "lents"), ("acteurs réels", "OVH, Scaleway"), "la souveraineté se pratique", winner="right"),
    "L'initiative européenne pour un cloud et des données souverains.",
    "The European initiative for sovereign cloud and data.")
add("eurohpc", lambda c: brand(c, "EuroHPC", "supercalculateurs publics · Jean Zay", "Europe"),
    "Les supercalculateurs européens mutualisés pour l'IA souveraine.",
    "European pooled supercomputers for sovereign AI.")
add("france-2030", lambda c: hub(c, "france 2030", "INVESTIR", ["calcul", "talents", "startups"], "le marché seul ne produirait pas de souveraineté"),
    "Le plan d'investissement français, dont un volet IA.",
    "The French investment plan, with an AI component.")
add("ecosysteme-ia-francais", lambda c: flow(c, "écosystème ia français", [("Mistral", POS), ("OVHcloud", POS), "intégration"], "bâtir de bout en bout sans les géants US"),
    "Une chaîne française complète, du modèle à l'hébergement souverain.",
    "A complete French chain, from model to sovereign hosting.")
add("sommets-ia", lambda c: hub(c, "sommets sur l'ia", "GOUVERNANCE", ["sûreté", "régulation", "coopération"], "l'IA mondiale, une gouvernance collective"),
    "Les rencontres internationales sur la gouvernance de l'IA.",
    "International gatherings on AI governance.")

# Outils / termes hérités
add("api", lambda c: flow(c, "api", ["application", "API", "modèle"], "connecter à OpenAI, c'est router vos prompts aux US"),
    "L'interface technique par laquelle deux logiciels communiquent.",
    "The technical interface through which two pieces of software communicate.")
add("big-tech", lambda c: bars(c, "big tech · cloud mondial", [("AWS/Azure/GCP", 0.65, INK), ("autres", 0.35, POS)], "~65% du marché, dépendance critique"),
    "Les géants technologiques américains dominant cloud et IA.",
    "The American tech giants dominating cloud and AI.")
add("cloud-act", lambda c: boundary(c, "cloud act", ["données", "Azure FR"], "portée du droit américain, même en France", out="→ US"),
    "La loi américaine réclamant les données des entreprises US, même à l'étranger.",
    "The US law claiming US companies' data, even abroad.")
add("open-source-ia", lambda c: compare(c, "open source ia", ("poids ouverts", "utilisable"), ("licence", "à vérifier"), "la licence est la première chose à vérifier", winner=None),
    "Un modèle dont les poids sont publiquement disponibles.",
    "A model whose weights are publicly available.")
add("outils-proprietaires", lambda c: compare(c, "outils propriétaires", ("performance", "supérieure"), ("dépendance", "totale"), "le fournisseur décide, vous subissez", winner=None),
    "Des modèles fermés, conditionnés à une licence commerciale.",
    "Closed models, subject to a commercial licence.")
add("deploiement-ia", lambda c: flow(c, "déploiement ia", ["prototype", "infra + gouvernance", "production"], "90% des projets n'atteignent pas la production"),
    "La mise en service opérationnelle d'un système d'IA.",
    "The operational rollout of an AI system.")
add("hebergement-delegue", lambda c: flow(c, "hébergement délégué", ["votre IA", "géré par un tiers", "monitoring 24/7"], "la souveraineté sans équipe DevOps"),
    "Un prestataire gère l'infrastructure IA pour le compte du client.",
    "A provider manages the AI infrastructure for the client.")
add("dsi", lambda c: hub(c, "direction des systèmes d'information", "DSI", ["infra", "sécurité", "TCO"], "co-construire dès le premier jour"),
    "La direction responsable de la stratégie des systèmes informatiques.",
    "The department responsible for IT systems strategy.")
add("tco", lambda c: compare(c, "coût total de possession", ("abonnement", "60$/mois"), ("+ intégration, sortie", "TCO réel"), "les solutions \"moins chères\" ne le sont pas", winner=None),
    "Le coût total incluant intégration, formation, maintenance, sortie.",
    "The total cost including integration, training, maintenance, exit.")
add("power-bi", lambda c: brand(c, "Power BI", "de la donnée à la décision", "Microsoft"),
    "L'outil de visualisation et d'analyse de données de Microsoft.",
    "Microsoft's data visualisation and analysis tool.")
add("dax", lambda c: brand(c, "DAX", "KPI complexes · piège des contextes", "Power BI"),
    "Le langage de formules de Power BI pour des mesures avancées.",
    "Power BI's formula language for advanced measures.")
add("coaching-pragmaforma", lambda c: flow(c, "coaching", ["question", "expert en direct", "cas concret"], "3 sessions valent 20h de vidéo"),
    "L'accompagnement personnalisé d'un apprenant par un expert.",
    "The personalised support of a learner by an expert.")
add("communaute-pragmaforma", lambda c: hub(c, "communauté", "RÉSEAU", ["pairs", "formateurs", "experts"], "réponse en moins de 24h, à vie"),
    "Un réseau de pairs échangeant autour d'un domaine de compétence.",
    "A network of peers exchanging around a field of expertise.")
add("mooc", lambda c: compare(c, "mooc", ("des notions", "regarder"), ("formation accompagnée", "faire"), "la différence entre regarder et faire", winner="right"),
    "Un cours en ligne massif, sans accompagnement individuel.",
    "A massive online course, without individual support.")
add("webinaire", lambda c: flow(c, "webinaire", ["présentation", "démonstration", "questions"], "un bon webinaire fait découvrir, ne vend pas"),
    "Une conférence pédagogique en direct sur internet.",
    "A live educational conference on the internet.")
add("jury-certification", lambda c: flow(c, "jury de certification", ["cas concret", "soutenance", "compétence validée ✓"], "une certification qui se mérite"),
    "L'évaluation finale par un panel d'experts indépendants.",
    "The final assessment by a panel of independent experts.")
add("ori-ia", lambda c: hub(c, "atelier ori-ia", "PROJET IA", ["Opportunités", "Risques", "Impacts"], "librement réutilisable chez vos clients"),
    "La méthode PragmaForma pour cartographier un projet d'IA.",
    "PragmaForma's method to map an AI project.")
add("synchrone-asynchrone", lambda c: compare(c, "synchrone / asynchrone", ("async", "à son rythme"), ("sync", "structure, lien"), "70-80% async pour les actifs", winner=None),
    "Deux modalités pédagogiques complémentaires.",
    "Two complementary learning formats.")
