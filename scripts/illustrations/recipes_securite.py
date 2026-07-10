# -*- coding: utf-8 -*-
"""Recettes d'illustration · thème sécurité."""
from helpers import flow, compare, boundary, shield, layers, hub, beforeafter
from primitives import INK, POS, GOLD, DIM

R = {}


def add(slug, fn, af, ae):
    R[slug] = (fn, af, ae)


add("anssi", lambda c: shield(c, "anssi", "SÉCURITÉ\nÉTAT", "référentiels publics · SecNumCloud"),
    "L'ANSSI protège l'État par des référentiels de cybersécurité publics.",
    "ANSSI protects the state with public cybersecurity frameworks.")

add("attaque-adverse", lambda c: beforeafter(c, "attaque adverse", ("panneau STOP", "+ pixels"), ("lu : 90 km/h", None), "quelques pixels trompent le modèle"),
    "Une attaque adverse altère imperceptiblement une entrée pour tromper le modèle.",
    "An adversarial attack imperceptibly alters an input to fool the model.")

add("calcul-multipartite", lambda c: flow(c, "calcul multipartite sécurisé", ["partie A", "partie B", "partie C"], "résultat commun sans révéler les données", hl=None),
    "Plusieurs parties calculent un résultat commun sans révéler leurs données.",
    "Several parties compute a joint result without revealing their data.")

add("chaine-approvisionnement", lambda c: flow(c, "chaîne d'approvisionnement ia", [("modèle", GOLD), ("données", GOLD), ("librairies", INK)], "un maillon compromis infecte tout l'aval"),
    "Chaque maillon de la chaîne IA peut être compromis en amont.",
    "Each link of the AI chain can be compromised upstream.")

add("chiffrement", lambda c: compare(c, "chiffrement", ("texte clair", "lisible"), ("chiffré", "illisible"), "qui détient les clés ?", winner="right"),
    "Le chiffrement rend les données illisibles sans la clé.",
    "Encryption makes data unreadable without the key.")

add("chiffrement-homomorphe", lambda c: boundary(c, "chiffrement homomorphe", ["calcul sur", "données", "chiffrées"], "le prestataire calcule sans jamais lire"),
    "Le chiffrement homomorphe calcule directement sur des données chiffrées.",
    "Homomorphic encryption computes directly on encrypted data.")

add("classification-information", lambda c: layers(c, "classification de l'information", [("SECRET", INK), ("CONFIDENTIEL", GOLD), ("INTERNE", POS), ("PUBLIC", DIM)], "quelles données dans quel outil ?"),
    "Classer l'information par sensibilité conditionne les usages IA autorisés.",
    "Classifying information by sensitivity conditions authorised AI uses.")

add("confidentialite-differentielle", lambda c: beforeafter(c, "confidentialité différentielle", "données réelles", ("+ bruit calibré", None), "impossible de savoir si vous y êtes"),
    "Un bruit calibré empêche de savoir si les données d'une personne ont servi.",
    "Calibrated noise prevents knowing whether a person's data was used.")

add("empoisonnement-donnees", lambda c: flow(c, "empoisonnement de données", [("données", INK), ("[piégées]", INK), ("modèle", DIM)], "corrompre l'entraînement pour dévier le modèle", hl=1),
    "Empoisonner les données d'entraînement modifie le comportement du modèle.",
    "Poisoning training data alters the model's behaviour.")

add("exfiltration", lambda c: boundary(c, "exfiltration", ["données", "internes"], "un agent piégé les fait sortir", out="→ dehors"),
    "L'exfiltration fait sortir des données hors du périmètre, souvent via un agent.",
    "Exfiltration moves data out of the perimeter, often via an agent.")

add("extraction-modele", lambda c: flow(c, "extraction de modèle", ["requêtes ×N", "réponses", "modèle copie"], "reconstituer un modèle en l'interrogeant"),
    "Interroger massivement une API permet de recopier le modèle.",
    "Massively querying an API allows copying the model.")

add("fraude-ia", lambda c: hub(c, "fraude augmentée par ia", "FRAUDE", ["voix clonée", "deepfake", "faux docs", "phishing"], "le coût de la tromperie s'effondre"),
    "L'IA démultiplie la fraude : voix clonées, deepfakes, faux documents.",
    "AI multiplies fraud: cloned voices, deepfakes, fake documents.")

add("fuite-informations", lambda c: flow(c, "fuite d'information", ["RAG", "réponse", "doc interdit"], "un défaut d'accès expose des documents", hl=2),
    "Un RAG mal cloisonné expose des documents au-delà des droits de l'utilisateur.",
    "A poorly compartmentalised RAG exposes documents beyond the user's rights.")

add("hameconnage-ia", lambda c: beforeafter(c, "hameçonnage augmenté par ia", ("email fautif", "repérable"), ("email parfait", "crédible"), "vérifier par un second canal"),
    "L'IA produit des courriels d'hameçonnage sans fautes, personnalisés à grande échelle.",
    "AI produces error-free, personalised phishing emails at scale.")

add("ia-fantome", lambda c: boundary(c, "ia fantôme", ["comptes", "perso"], "usage hors de tout cadre validé", out="hors contrôle"),
    "L'IA fantôme : usage d'outils IA hors de tout cadre validé par l'organisation.",
    "Shadow AI: use of AI tools outside any framework validated by the organisation.")

add("iam", lambda c: flow(c, "gestion des identités et accès", ["identité", "droits", "ressource"], "l'IA hérite des droits, elle ne les crée pas"),
    "L'IAM détermine qui accède à quoi ; l'IA hérite des droits existants.",
    "IAM determines who accesses what; AI inherits existing rights.")

add("inference-appartenance", lambda c: flow(c, "inférence d'appartenance", ["profil", "modèle", "\"a été vu\""], "déduire qu'une personne était dans l'entraînement", hl=2),
    "Déterminer si les données d'une personne ont servi à entraîner un modèle.",
    "Determining whether a person's data was used to train a model.")

add("injection-indirecte", lambda c: flow(c, "injection indirecte", [("page web", INK), ("[ordre caché]", INK), ("agent", DIM)], "le monde extérieur n'est pas de confiance", hl=1),
    "Des instructions cachées dans un contenu consulté détournent l'agent.",
    "Hidden instructions in consulted content hijack the agent.")

add("inversion-modele", lambda c: flow(c, "inversion de modèle", ["modèle", "reconstruction", "données source"], "le modèle peut trahir ses données d'entraînement"),
    "Reconstruire les données d'entraînement à partir du modèle.",
    "Reconstructing training data from the model.")

add("jailbreak", lambda c: beforeafter(c, "débridage (jailbreak)", ("demande directe", "refusée"), ("jeu de rôle", "contournée"), "les garde-fous sont des probabilités"),
    "Le débridage contourne les garde-fous par des prompts astucieux.",
    "Jailbreaking bypasses guardrails through clever prompts.")

add("journalisation", lambda c: flow(c, "journalisation", ["prompt", "sources", "réponse"], "sans trace, pas d'audit ni de responsabilité"),
    "Enregistrer les événements d'un système IA conditionne son auditabilité.",
    "Logging an AI system's events conditions its auditability.")

add("moindre-privilege", lambda c: compare(c, "moindre privilège", ("tous droits", "risqué"), ("droits minimaux", "sûr"), "pourquoi autoriser, pas pourquoi restreindre", winner="right"),
    "Un agent ne reçoit que les droits strictement nécessaires à sa tâche.",
    "An agent receives only the rights strictly necessary for its task.")

add("owasp-llm", lambda c: layers(c, "owasp top 10 · llm", [("injection de prompt", INK), ("fuite d'infos", INK), ("chaîne d'appro.", GOLD), ("autonomie excessive", GOLD)], "la check-list de référence des équipes sécurité"),
    "Le top 10 OWASP recense les vulnérabilités critiques des applications LLM.",
    "The OWASP Top 10 lists the critical vulnerabilities of LLM applications.")

add("porte-derobee-modele", lambda c: flow(c, "porte dérobée", ["modèle normal", "[déclencheur]", "comportement caché"], "indétectable par les tests standards", hl=1),
    "Un comportement malveillant caché, activé par un déclencheur précis.",
    "A hidden malicious behaviour, activated by a specific trigger.")

add("red-teaming", lambda c: flow(c, "red teaming", ["attaquer soi-même", "trouver les failles", "corriger"], "avant que les vrais attaquants ne le fassent", loop=True),
    "Attaquer volontairement son IA pour trouver les failles avant les attaquants.",
    "Deliberately attacking your AI to find flaws before attackers do.")

add("secnumcloud", lambda c: shield(c, "secnumcloud", "CLOUD DE\nCONFIANCE", "immunité au CLOUD Act · label ANSSI"),
    "Le label ANSSI du cloud de confiance, immunisé aux lois extraterritoriales.",
    "The ANSSI trusted-cloud label, immune to extraterritorial laws.")

add("securite-donnees", lambda c: shield(c, "sécurité des données", "DONNÉES", "chiffrement · droits · non-réutilisation"),
    "Protéger les données contre accès non autorisés, fuites et altérations.",
    "Protecting data against unauthorised access, leaks and tampering.")

add("sso", lambda c: hub(c, "authentification unique", "SSO", ["assistant", "RAG", "outils", "annuaire"], "une identité, propagée partout"),
    "S'authentifier une fois pour accéder à plusieurs applications.",
    "Authenticating once to access several applications.")

add("tee", lambda c: boundary(c, "environnement d'exécution de confiance", ["code +", "données", "protégés"], "la confidentialité repose sur le matériel"),
    "Une zone matérielle isolée protège code et données, même de l'administrateur.",
    "An isolated hardware zone protects code and data, even from the administrator.")

add("test-intrusion", lambda c: flow(c, "test d'intrusion", ["simuler l'attaque", "trouver la faille", "corriger avant"], "web classique + failles propres à l'IA"),
    "Simuler une attaque réelle pour éprouver les défenses d'une application IA.",
    "Simulating a real attack to test an AI application's defences.")

add("zero-trust", lambda c: flow(c, "zéro confiance", ["agent", "service", "données"], "chaque appel prouve son identité et ses droits"),
    "Ne jamais faire confiance par défaut : chaque accès est vérifié.",
    "Never trust by default: every access is verified.")
