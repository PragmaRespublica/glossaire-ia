# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème cadre juridique."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter, meter
from primitives import INK, POS, GOLD, DIM

R = {}
def add(s, fn, af, ae): R[s] = (fn, af, ae)

add("systeme-haut-risque", lambda c: layers(c, "système à haut risque", [("DOCUMENTATION", INK), ("SUPERVISION HUMAINE", INK), ("ANALYSE D'IMPACT", GOLD)], "obligations les plus lourdes de l'AI Act"),
    "Un système à haut risque cumule les obligations les plus lourdes.",
    "A high-risk system carries the heaviest obligations.")
add("pratiques-interdites", lambda c: shield(c, "pratiques interdites", "RISQUE\nINACCEPTABLE", "notation sociale · manipulation · interdit"),
    "Les usages d'IA à risque inacceptable, interdits dans l'Union.",
    "AI uses of unacceptable risk, banned in the Union.")
add("gpai", lambda c: flow(c, "modèle à usage général", ["fournisseur", "obligations", "intégrateurs"], "responsabiliser l'amont de la chaîne"),
    "Un modèle à usage général, aux obligations propres sous l'AI Act.",
    "A general-purpose model with specific obligations under the AI Act.")
add("bureau-ia", lambda c: hub(c, "bureau européen de l'ia", "AI OFFICE", ["autorités", "codes", "sanctions"], "donne du mordant à l'AI Act"),
    "L'organe supervisant l'AI Act, notamment les modèles à usage général.",
    "The body overseeing the AI Act, notably general-purpose models.")
add("marquage-ce", lambda c: flow(c, "marquage ce", ["évaluation", "documentation", "CE ✓"], "sans marquage, pas de mise sur le marché"),
    "Le marquage CE atteste la conformité d'un système à haut risque.",
    "CE marking certifies a high-risk system's conformity.")
add("fria", lambda c: flow(c, "analyse d'impact · droits fondamentaux", ["système", "risques", "atténuation"], "expliciter des arbitrages implicites"),
    "L'analyse d'impact des systèmes à haut risque sur les droits fondamentaux.",
    "The impact assessment of high-risk systems on fundamental rights.")
add("aipd", lambda c: flow(c, "analyse d'impact · rgpd", ["traitement", "risques", "mesures"], "le garde-corps, mené tôt"),
    "L'étude d'impact imposée avant un traitement à risque élevé.",
    "The impact study required before a high-risk processing.")
add("dpo-delegue", lambda c: hub(c, "délégué à la protection des données", "DPO", ["conseille", "contrôle", "CNIL"], "un accélérateur, pas un frein"),
    "Le DPO veille à la conformité des traitements de données personnelles.",
    "The DPO ensures personal data processing complies.")
add("cnil", lambda c: shield(c, "cnil", "PROTECTION\nDES DONNÉES", "un cadre, pas un ennemi de l'innovation"),
    "L'autorité française de protection des données personnelles.",
    "France's personal data protection authority.")
add("base-legale", lambda c: layers(c, "base légale", [("consentement", GOLD), ("contrat", INK), ("intérêt légitime", POS)], "la première décision juridique du projet"),
    "Le fondement qui rend licite un traitement de données personnelles.",
    "The ground that makes personal data processing lawful.")
add("consentement", lambda c: compare(c, "consentement", ("pré-coché", "invalide"), ("libre, retirable", "valide"), "la base la plus fragile", winner="right"),
    "Une acceptation libre, spécifique, éclairée et univoque.",
    "A free, specific, informed and unambiguous acceptance.")
add("droits-personnes", lambda c: hub(c, "droits des personnes", "RGPD", ["accès", "rectif.", "effacement", "opposition"], "le test de réalité d'un projet IA"),
    "Accès, rectification, effacement, opposition : les droits garantis.",
    "Access, rectification, erasure, objection: the guaranteed rights.")
add("decision-automatisee", lambda c: flow(c, "décision automatisée", [("score IA", INK), "humain", "décision"], "droit à une intervention humaine réelle", hl=1),
    "L'article 22 encadre les décisions prises sans intervention humaine.",
    "Article 22 frames decisions made without human intervention.")
add("supervision-humaine", lambda c: flow(c, "supervision humaine", ["système", "humain outillé", "intervenir / arrêter"], "présent ET capable de juger", hl=1),
    "Le système doit être effectivement supervisable par un humain.",
    "The system must be effectively supervisable by a human.")
add("transferts-internationaux", lambda c: boundary(c, "transferts internationaux", ["données", "UE"], "chaque appel hors UE vous engage", out="→ hors UE"),
    "La sortie de données hors de l'UE, enjeu central des API américaines.",
    "The exit of data outside the EU, key issue of American APIs.")
add("data-privacy-framework", lambda c: compare(c, "data privacy framework", ("cadre actuel", "licite"), ("2 prédécesseurs", "annulés"), "ne pas tout bâtir dessus", winner=None),
    "L'accord UE-États-Unis, historiquement instable.",
    "The EU-US agreement, historically unstable.")
add("clauses-contractuelles", lambda c: compare(c, "clauses contractuelles types", ("signature", "papier"), ("droit local", "vérité"), "un contrat ne suspend pas une loi", winner="right"),
    "Des clauses types encadrant les transferts, à compléter d'une analyse.",
    "Standard clauses framing transfers, to complete with an analysis.")
add("dsa-dma", lambda c: compare(c, "dsa · dma", ("modération", "transparence"), ("concurrence", "loyauté"), "l'IA des plateformes devient auditable", winner=None),
    "Deux règlements encadrant les grandes plateformes numériques.",
    "Two regulations framing large digital platforms.")
add("data-act", lambda c: flow(c, "data act", ["objet connecté", "vos données", "vos modèles"], "une arme anti-verrouillage"),
    "Le règlement rendant les données des objets connectés portables.",
    "The regulation making connected-device data portable.")
add("nis2", lambda c: shield(c, "directive nis 2", "CYBER-\nSÉCURITÉ", "responsabilité des dirigeants"),
    "La directive renforçant la cybersécurité d'un large éventail d'acteurs.",
    "The directive strengthening cybersecurity for a broad range of actors.")
add("exception-tdm", lambda c: compare(c, "exception de fouille (tdm)", ("opt-out exprimé", "protégé"), ("silence", "fouille permise"), "le nœud juridique de l'entraînement", winner="left"),
    "L'exception autorisant la fouille de contenus pour entraîner les modèles.",
    "The exception authorising content mining to train models.")
add("opt-out", lambda c: shield(c, "opt-out", "RÉSERVATION\nDES DROITS", "machine-lisible = opposable"),
    "Le droit de refuser que ses contenus servent à entraîner l'IA.",
    "The right to refuse one's content being used to train AI.")
add("statut-oeuvres-ia", lambda c: compare(c, "statut des œuvres ia", ("100% IA", "non protégée"), ("apport humain", "protégeable"), "la valeur réside dans votre apport", winner="right"),
    "La protection des contenus générés dépend de l'intervention humaine.",
    "The protection of generated content depends on human intervention.")
add("responsabilite-ia", lambda c: flow(c, "responsabilité de l'ia", ["fournisseur", "intégrateur", "déployeur"], "se règle dans les contrats, avant l'incident"),
    "Qui répond des dommages : fournisseur, intégrateur ou déployeur ?",
    "Who is liable for harm: provider, integrator or deployer?")
add("iso-42001", lambda c: shield(c, "iso/iec 42001", "MANAGEMENT\nDE L'IA", "un cadre prêt à l'emploi"),
    "La norme de système de management de l'IA, comme ISO 27001.",
    "The AI management system standard, like ISO 27001.")
add("nist-ai-rmf", lambda c: layers(c, "nist ai rmf", [("cartographier", INK), ("mesurer", INK), ("gérer", GOLD), ("gouverner", POS)], "méthode souple, complète l'AI Act"),
    "Le cadre volontaire du NIST pour gérer les risques de l'IA.",
    "The NIST voluntary framework for managing AI risks.")
add("normes-harmonisees", lambda c: flow(c, "normes harmonisées", ["exigence AI Act", "norme technique", "présomption ✓"], "la traduction opérationnelle des obligations"),
    "Les normes précisant comment respecter concrètement l'AI Act.",
    "Standards specifying how to concretely meet the AI Act.")
add("certification-ia", lambda c: flow(c, "certification ia", ["système", "évaluation", "certificat ✓"], "un différenciateur de marché"),
    "Attester qu'un système d'IA respecte un référentiel donné.",
    "Certifying that an AI system complies with a given framework.")
add("conformite-ia", lambda c: flow(c, "conformité ia", ["inventaire", "classement risque", "plan d'action"], "cartographier avant de réglementer"),
    "S'assurer que ses usages d'IA respectent le droit applicable.",
    "Ensuring your AI uses comply with applicable law.")
add("accountability", lambda c: shield(c, "responsabilité démontrable", "PROUVER LA\nCONFORMITÉ", "l'accountability se prépare"),
    "Ne pas seulement respecter les règles, mais pouvoir le prouver.",
    "Not only respecting the rules, but being able to prove it.")
add("registre-cas-usage", lambda c: flow(c, "registre des cas d'usage", ["23 usages", "3 haut risque", "5 à régulariser"], "le premier livrable de la gouvernance IA"),
    "L'inventaire à jour de tous les usages d'IA d'une organisation.",
    "The up-to-date inventory of all an organisation's AI uses.")
add("registre-traitements", lambda c: flow(c, "registre des traitements", ["finalités", "données", "sécurité"], "on y découvre les usages non déclarés"),
    "Le document RGPD recensant tous les traitements de données.",
    "The GDPR document listing all data processing operations.")
add("comite-ia", lambda c: hub(c, "comité ia", "COMITÉ", ["DSI", "DPO", "RSSI", "métiers"], "un accélérateur, pas un tribunal"),
    "L'instance interne qui arbitre les projets d'IA.",
    "The internal body arbitrating AI projects.")
add("clauses-ia-contrats", lambda c: layers(c, "clauses ia dans les contrats", [("non-réutilisation", POS), ("localisation UE", POS), ("réversibilité", POS)], "négociez tant que vous avez le pouvoir"),
    "Les clauses cadrant l'IA dans les contrats fournisseurs.",
    "The clauses framing AI in vendor contracts.")
add("codes-conduite-gpai", lambda c: flow(c, "codes de bonnes pratiques gpai", ["transparence", "droit d'auteur", "sûreté"], "le droit souple qui précède le droit dur"),
    "Les codes précisant les obligations des modèles à usage général.",
    "The codes specifying general-purpose models' obligations.")
add("bac-sable-reglementaire", lambda c: boundary(c, "bac à sable réglementaire", ["tester", "sous", "supervision"], "innovateur et régulateur apprennent ensemble"),
    "Un dispositif encadré pour tester une innovation IA en conditions réelles.",
    "A supervised mechanism to test an AI innovation in real conditions.")
add("signalement-incidents", lambda c: flow(c, "signalement des incidents", ["incident grave", "notification", "mesures"], "une mémoire collective des défaillances"),
    "L'obligation de notifier les incidents graves des systèmes à haut risque.",
    "The obligation to report serious incidents of high-risk systems.")
add("surveillance-travail", lambda c: compare(c, "surveillance au travail", ("productivité IA", "?"), ("droits, dignité", "!"), "un champ de mines juridique et humain", winner="right"),
    "La surveillance algorithmique des salariés, fortement encadrée.",
    "Algorithmic employee surveillance, strongly framed.")
add("privacy-by-design", lambda c: beforeafter(c, "protection dès la conception", ("conformité après", "coûteux"), ("dès la conception", "gratuit"), "décidez tôt"),
    "Intégrer la protection des données dès la conception d'un système.",
    "Building data protection into a system's design.")
add("acculturation-ia", lambda c: flow(c, "acculturation à l'ia", ["former", "comprendre", "usage éclairé"], "obligation de l'AI Act depuis 2025"),
    "Le niveau de maîtrise de l'IA, désormais une obligation légale.",
    "The level of AI literacy, now a legal obligation.")
add("c2pa", lambda c: shield(c, "c2pa", "PROVENANCE\nDU CONTENU", "métadonnées signées cryptographiquement"),
    "Le standard attachant à un fichier une preuve d'origine vérifiable.",
    "The standard attaching verifiable origin proof to a file.")
add("filigrane-ia", lambda c: compare(c, "filigrane (watermarking)", ("marque insérée", "signal"), ("recadrage", "effacée"), "nécessaire mais fragile", winner=None),
    "Insérer dans un contenu IA une marque signalant son origine.",
    "Inserting into AI content a mark signalling its origin.")
add("hds", lambda c: shield(c, "hébergement de données de santé", "HDS", "le préalable de toute IA médicale"),
    "La certification obligatoire pour héberger des données de santé.",
    "The mandatory certification to host health data.")
add("identification-biometrique", lambda c: compare(c, "identification biométrique", ("nécessaire ?", "?"), ("proportionné ?", "?"), "souvent, une solution moins intrusive suffit", winner=None),
    "Reconnaître une personne par ses caractéristiques physiques, très encadré.",
    "Recognising a person by physical characteristics, strictly framed.")
add("reconnaissance-faciale", lambda c: compare(c, "reconnaissance faciale", ("déverrouiller", "consenti"), ("surveiller foule", "encadré"), "l'usage fait la frontière", winner="left"),
    "Deux mondes juridiques opposés selon consentement et centralisation.",
    "Two opposed legal worlds by consent and centralisation.")
add("notation-sociale", lambda c: shield(c, "notation sociale", "INTERDIT", "une ligne rouge de l'AI Act"),
    "Noter les individus pour conditionner leurs droits : interdit.",
    "Scoring individuals to condition their rights: banned.")
add("police-predictive", lambda c: flow(c, "police prédictive", ["données biaisées", "prédiction", "+ patrouilles"], "une prophétie autoréalisatrice", loop=True),
    "L'IA prédisant les infractions, un biais qui s'auto-entretient.",
    "AI predicting offences, a self-reinforcing bias.")
add("reconnaissance-emotions", lambda c: compare(c, "reconnaissance des émotions", ("interdite au travail", "!"), ("base scientifique", "douteuse"), "vendre une lecture des âmes", winner=None),
    "Prétendre déduire les émotions, contesté et souvent interdit.",
    "Claiming to infer emotions, contested and often banned.")
add("charte-ia", lambda c: layers(c, "charte ia", [("autorisé", POS), ("encadré", GOLD), ("interdit", INK)], "autorise explicitement, pas seulement interdit"),
    "Le document encadrant l'usage de l'IA dans une organisation.",
    "The document framing AI use in an organisation.")
add("cpf", lambda c: flow(c, "cpf · financement", ["solde CPF", "formation éligible", "prise en charge"], "un paysage complexe, contactez-nous"),
    "Le Compte Personnel de Formation finance une formation certifiée.",
    "The personal training account funds a certified programme.")
add("droits-auteur-ia", lambda c: compare(c, "droits d'auteur & ia", ("entraînement", "sources ?"), ("œuvres générées", "titularité ?"), "l'un des chantiers les plus instables", winner=None),
    "Les questions juridiques sur l'entraînement et les œuvres générées.",
    "The legal questions on training and generated works.")
add("ethique-ia", lambda c: hub(c, "éthique de l'ia", "ÉTHIQUE", ["équité", "transparence", "responsabilité"], "un levier qualité, pas une contrainte"),
    "La réflexion sur les implications morales de l'IA.",
    "The reflection on AI's moral implications.")
add("gouvernance-ia", lambda c: hub(c, "gouvernance de l'ia", "PILOTAGE", ["comité", "registre", "revue"], "un processus court, pas un comité Théodule"),
    "Les structures et règles encadrant l'usage de l'IA.",
    "The structures and rules framing AI use.")
