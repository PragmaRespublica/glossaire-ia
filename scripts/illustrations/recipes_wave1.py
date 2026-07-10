# -*- coding: utf-8 -*-
"""
Recettes d'illustration · vague 1 (représentative des 10 thèmes).
Chaque recette : slug -> (fonction(c), alt_fr, alt_en).
Métaphores conceptuelles originales, style blueprint PragmaForma.
"""
from primitives import INK, POS, DIM, GOLD

R = {}


def rec(slug, alt_fr, alt_en):
    def deco(fn):
        R[slug] = (fn, alt_fr, alt_en)
        return fn
    return deco


# ── RAG & agents ────────────────────────────────────────────────────────
@rec("rag",
     "Schéma d'un RAG : une base documentaire alimente une recherche, dont les passages rejoignent la question vers un modèle qui produit une réponse sourcée.",
     "RAG diagram: a document base feeds a search whose passages join the question into a model producing a sourced answer.")
def _(c):
    c.eyebrow("retrieval-augmented generation")
    c.node(70, 120, 110, 46, "DOCS", sub="base")
    c.line(180, 143, 235, 143, arrow=True)
    c.node(235, 120, 110, 46, "RECHERCHE", size=11)
    c.line(345, 143, 400, 143, arrow=True)
    c.node(400, 108, 120, 70, "LLM", size=16)
    c.line(460, 178, 460, 210, arrow=True)
    c.text(460, 232, '"réponse sourcée"', size=12, anchor="middle", italic=True, color=POS)
    c.text(290, 200, "sens > mots-clés", size=11, anchor="middle", op=0.5)


@rec("agent-ia",
     "Boucle d'un agent : penser, agir, observer, recommencer jusqu'à atteindre l'objectif.",
     "Agent loop: think, act, observe, repeat until the goal is reached.")
def _(c):
    c.eyebrow("boucle agentique")
    for i, (lab, x) in enumerate([("PENSER", 120), ("AGIR", 270), ("OBSERVER", 410)]):
        c.node(x, 120, 110, 46, lab, size=12)
        if i < 2:
            c.line(x + 110, 143, x + 150, 143, arrow=True)
    c.path("M 465 166 q 40 60 -150 70 q -190 0 -170 -70", stroke=INK, sw=2, dash="5 4", arrow=True)
    c.text(300, 250, "itérer", size=12, anchor="middle", op=0.6)


@rec("vector-store",
     "Base vectorielle : des documents deviennent des points dans un espace, et une requête retrouve les plus proches.",
     "Vector store: documents become points in a space, and a query retrieves the nearest ones.")
def _(c):
    c.eyebrow("base vectorielle")
    c.rect(90, 70, 300, 190, rx=6, sop=0.5)
    pts = [(140, 120), (180, 200), (250, 110), (320, 170), (210, 150), (300, 230), (150, 240)]
    for x, y in pts:
        c.circle(x, y, 4, fill=INK, stroke="none", op=0.7)
    q = (240, 165)
    c.circle(*q, 6, fill=POS, stroke="none")
    for x, y in [(250, 110), (210, 150), (320, 170)]:
        c.line(q[0], q[1], x, y, stroke=POS, sw=1.4, dash="3 3")
    c.text(q[0], q[1] + 26, "requête", size=11, anchor="middle", color=POS)
    c.node(430, 140, 110, 46, "TOP-K", size=13)
    c.line(390, 165, 428, 165, arrow=True)


# ── Architecture & modèles ──────────────────────────────────────────────
@rec("llm",
     "Un grand modèle de langage prédit le prochain fragment de texte, token après token.",
     "A large language model predicts the next fragment of text, token after token.")
def _(c):
    c.eyebrow("grand modèle de langage")
    c.node(70, 110, 150, 90, "", size=14)
    c.text(145, 150, "N milliards", size=13, anchor="middle")
    c.text(145, 172, "de paramètres", size=11, anchor="middle", op=0.6)
    c.line(220, 155, 265, 155, arrow=True)
    toks = ["le", "chat", "mange", "la", "___"]
    for i, t in enumerate(toks):
        col = POS if t == "___" else INK
        c.node(275 + i * 58, 132, 52, 44, t, size=12, color=col,
               dash="4 3" if t == "___" else None)
    c.text(275 + 4 * 58 + 26, 200, "prochain\ntoken", size=10, anchor="middle", color=POS, op=0.8)
    c.text(490, 210, "?", size=16, anchor="middle", color=POS)


@rec("token",
     "Tokenisation : une phrase est découpée en unités élémentaires facturées et traitées par le modèle.",
     "Tokenisation: a sentence is split into elementary units billed and processed by the model.")
def _(c):
    c.eyebrow("tokenisation")
    c.text(300, 95, '"comprendre l\'IA"', size=15, anchor="middle", op=0.8)
    c.line(300, 108, 300, 132, arrow=True)
    chunks = ["compr", "endre", "l'", "IA"]
    x = 150
    for ch in chunks:
        w = 22 + len(ch) * 13
        c.node(x, 150, w, 46, ch, size=13)
        x += w + 10
    c.text(300, 230, f"{len(chunks)} tokens · facturés à l'usage", size=12,
           anchor="middle", op=0.6)


@rec("transformer",
     "Architecture transformer : chaque mot pondère l'importance de tous les autres par le mécanisme d'attention.",
     "Transformer architecture: each word weighs the importance of all others through the attention mechanism.")
def _(c):
    c.eyebrow("attention")
    words = ["l'", "avocat", "plaide", "au", "tribunal"]
    xs = [90 + i * 105 for i in range(len(words))]
    for x, w in zip(xs, words):
        c.node(x - 34, 200, 68, 40, w, size=12)
    focus = 1
    for j in range(len(words)):
        if j == focus:
            continue
        op = 0.7 if j in (4,) else 0.25
        c.path(f"M {xs[focus]} 200 Q {(xs[focus]+xs[j])/2} 120 {xs[j]} 200",
               stroke=INK, sw=1.6, sop=op)
    c.circle(xs[focus], 200, 22, stroke=POS, sw=2)
    c.text(300, 95, "chaque mot regarde tous les autres", size=12, anchor="middle", op=0.6)


@rec("embedding",
     "Un mot est projeté en vecteur ; les sens proches occupent des positions voisines dans l'espace.",
     "A word is projected into a vector; close meanings occupy neighbouring positions in space.")
def _(c):
    c.eyebrow("plongement vectoriel")
    c.line(90, 240, 380, 240, arrow=True, sop=0.5)
    c.line(90, 240, 90, 70, arrow=True, sop=0.5)
    def dot(x, y, lab, col=INK):
        c.circle(x, y, 5, fill=col, stroke="none")
        c.text(x + 10, y + 4, lab, size=12, color=col)
    dot(180, 120, "roi")
    dot(230, 105, "reine", POS)
    dot(300, 200, "pomme")
    dot(340, 185, "poire", POS)
    c.line(180, 120, 230, 105, stroke=POS, sw=1.3, dash="3 3")
    c.line(300, 200, 340, 185, stroke=POS, sw=1.3, dash="3 3")
    c.text(470, 160, "sens\n≈ distance", size=12, anchor="middle", op=0.7)


@rec("fine-tuning",
     "Le fine-tuning ajoute une fine couche d'adaptation à un modèle de base déjà entraîné.",
     "Fine-tuning adds a thin adaptation layer to an already-trained base model.")
def _(c):
    c.eyebrow("affinage")
    c.node(80, 110, 160, 90, "MODÈLE DE BASE", size=12)
    c.text(160, 175, "préentraîné", size=11, anchor="middle", op=0.5)
    c.text(270, 140, "+", size=24, anchor="middle")
    c.node(300, 125, 90, 60, "Δ", size=20, color=POS, dash="4 3")
    c.text(345, 200, "vos données", size=11, anchor="middle", color=POS, op=0.8)
    c.line(400, 155, 435, 155, arrow=True)
    c.node(445, 110, 110, 90, "MODÈLE\nSPÉCIALISÉ", size=11, color=POS)


@rec("ia-generative",
     "L'IA générative produit du contenu nouveau à partir d'une instruction en langage naturel.",
     "Generative AI produces new content from a natural-language instruction.")
def _(c):
    c.eyebrow("ia générative")
    c.text(120, 150, '"génère..."', size=14, anchor="middle", italic=True)
    c.line(190, 150, 245, 150, arrow=True)
    c.node(250, 115, 90, 70, "IA", size=18)
    c.line(340, 150, 380, 150, arrow=True)
    for i, lab in enumerate(["texte", "image", "son", "code"]):
        c.node(390, 90 + i * 34, 90, 28, lab, size=11, color=POS)


@rec("gpt",
     "GPT décompose trois idées : génératif, préentraîné, transformer.",
     "GPT decomposes into three ideas: generative, pre-trained, transformer.")
def _(c):
    c.eyebrow("g · p · t")
    for i, (a, b) in enumerate([("G", "génératif"), ("P", "préentraîné"), ("T", "transformer")]):
        x = 90 + i * 160
        c.node(x, 110, 120, 70, a, size=28)
        c.text(x + 60, 205, b, size=12, anchor="middle", op=0.7)
        if i < 2:
            c.text(x + 135, 150, "·", size=24, anchor="middle")


# ── Souveraineté ────────────────────────────────────────────────────────
@rec("ia-souveraine",
     "IA souveraine : les données restent à l'intérieur de la frontière, sous contrôle local.",
     "Sovereign AI: data stays inside the border, under local control.")
def _(c):
    c.eyebrow("ia souveraine")
    c.rect(150, 70, 300, 180, rx=8, dash="8 5")
    c.text(300, 60, "🇪🇺 périmètre maîtrisé", size=12, anchor="middle", op=0.6)
    c.node(200, 120, 90, 50, "DONNÉES", size=11)
    c.node(310, 120, 90, 50, "MODÈLE", size=11)
    c.line(290, 145, 310, 145, stroke=INK, sw=2)
    c.node(255, 190, 90, 40, "VOUS", size=12, color=POS)
    c.text(510, 150, "rien\nne sort", size=12, anchor="middle", color=POS)
    c.line(450, 160, 486, 160, stroke=INK, sw=2, arrow=True)
    c.cross(500, 200, INK, 6)


@rec("cloud-souverain",
     "Cloud souverain : un hébergeur européen hors de portée du droit extraterritorial.",
     "Sovereign cloud: a European host beyond the reach of extraterritorial law.")
def _(c):
    c.eyebrow("cloud souverain")
    c.node(90, 130, 130, 70, "OVHcloud\nScaleway", size=12, color=POS)
    c.text(155, 225, "droit européen", size=11, anchor="middle", op=0.6)
    c.node(380, 130, 130, 70, "CLOUD ACT", size=12, dash="5 4")
    c.text(445, 225, "portée US", size=11, anchor="middle", op=0.6)
    c.path("M 360 165 q -30 0 -40 0", stroke=INK, sw=2, arrow=True)
    c.cross(300, 165, INK, 8)
    c.text(300, 110, "hors d'atteinte", size=11, anchor="middle", color=POS, op=0.8)


@rec("souverainete-numerique",
     "Souveraineté numérique : garder les clés de ses choix technologiques.",
     "Digital sovereignty: keeping the keys to one's technological choices.")
def _(c):
    c.eyebrow("souveraineté numérique")
    c.circle(300, 150, 60, sw=2)
    c.path("M 300 120 a 16 16 0 1 1 -0.1 0 M 300 150 l 0 40 l 14 0 m -14 -18 l 10 0",
           stroke=INK, sw=2)
    c.text(300, 235, "maîtriser ses choix", size=12, anchor="middle", op=0.7)
    c.node(70, 130, 90, 40, "données", size=11, color=POS)
    c.node(70, 180, 90, 40, "modèles", size=11, color=POS)
    c.node(440, 130, 90, 40, "infra", size=11, color=POS)
    c.node(440, 180, 90, 40, "code", size=11, color=POS)


@rec("open-weights",
     "Modèle à poids ouverts : téléchargeable, exécutable et adaptable chez soi.",
     "Open-weights model: downloadable, runnable and adaptable at home.")
def _(c):
    c.eyebrow("poids ouverts")
    c.path("M 270 120 a 30 30 0 0 1 60 0", stroke=INK, sw=3)
    c.rect(255, 118, 90, 70, rx=6, sop=1)
    c.circle(300, 150, 7, fill=INK, stroke="none")
    c.line(300, 157, 300, 172, stroke=INK, sw=3)
    c.text(300, 210, "poids téléchargeables", size=12, anchor="middle", color=POS, op=0.9)
    c.line(300, 225, 300, 250, arrow=True)
    c.text(300, 272, "→ hébergé chez vous", size=11, anchor="middle", op=0.6)


# ── Réglementaire ───────────────────────────────────────────────────────
@rec("ai-act",
     "L'AI Act classe les systèmes en quatre niveaux de risque, de l'inacceptable au minimal.",
     "The AI Act classifies systems into four risk levels, from unacceptable to minimal.")
def _(c):
    c.eyebrow("ai act · niveaux de risque")
    levels = [("INACCEPTABLE", 200, INK), ("HAUT RISQUE", 150, INK),
              ("LIMITÉ", 100, GOLD), ("MINIMAL", 50, POS)]
    y = 90
    for lab, w, col in levels:
        x = 300 - w / 2
        c.rect(x, y, w, 34, rx=4, stroke=col, fill=col, op=0.1)
        c.text(300, y + 22, lab, size=11, anchor="middle", color=col)
        y += 42
    c.text(300, 275, "obligations proportionnées au risque", size=11, anchor="middle", op=0.5)


@rec("rgpd",
     "Le RGPD protège les données personnelles par un bouclier de droits.",
     "The GDPR protects personal data with a shield of rights.")
def _(c):
    c.eyebrow("rgpd")
    c.path("M 300 80 L 360 105 L 360 160 Q 360 210 300 235 Q 240 210 240 160 L 240 105 Z",
           stroke=INK, sw=2)
    c.text(300, 150, "DONNÉES\nPERSONNELLES", size=11, anchor="middle")
    c.check(288, 170, POS, 1.2)
    for i, lab in enumerate(["accès", "rectif.", "effacement", "opposition"]):
        c.text(300, 260 if i < 2 else 275, "", size=10)
    c.text(300, 262, "accès · rectification · effacement", size=10, anchor="middle", op=0.6)


@rec("hallucination",
     "Hallucination : une réponse fausse énoncée avec assurance, sans source.",
     "Hallucination: a false answer stated with confidence, with no source.")
def _(c):
    c.eyebrow("hallucination")
    c.node(120, 120, 120, 70, "LLM", size=16)
    c.line(240, 155, 285, 155, arrow=True)
    c.rect(295, 122, 190, 66, rx=6, dash="4 4")
    c.text(390, 150, '"la loi de 1987..."', size=13, anchor="middle", italic=True)
    c.text(390, 172, "(inventée)", size=11, anchor="middle", color=INK, op=0.7)
    c.cross(475, 135, INK, 7)
    c.text(390, 225, "confiant ≠ exact", size=12, anchor="middle", op=0.6)


@rec("biais-algorithmique",
     "Biais algorithmique : le modèle reproduit et amplifie les déséquilibres de ses données.",
     "Algorithmic bias: the model reproduces and amplifies its data's imbalances.")
def _(c):
    c.eyebrow("biais algorithmique")
    c.line(110, 230, 300, 230, sop=0.5)
    heights = [20, 35, 90, 120, 60, 25]
    for i, h in enumerate(heights):
        x = 120 + i * 28
        col = INK if h > 70 else DIM
        c.rect(x, 230 - h, 20, h, rx=2, stroke=col, fill=col, op=0.15)
    c.text(205, 255, "données déséquilibrées", size=10, anchor="middle", op=0.6)
    c.line(320, 150, 360, 150, arrow=True)
    c.node(370, 120, 120, 60, "MODÈLE", size=12)
    c.text(430, 200, "amplifie le biais", size=11, anchor="middle", color=INK, op=0.8)


@rec("benchmark",
     "Un benchmark compare les modèles sur des tâches standardisées, avec ses limites.",
     "A benchmark compares models on standardised tasks, with its limits.")
def _(c):
    c.eyebrow("benchmark")
    data = [("modèle A", 0.86, INK), ("modèle B", 0.81, POS), ("modèle C", 0.74, DIM)]
    for i, (lab, v, col) in enumerate(data):
        y = 100 + i * 46
        c.text(160, y + 16, lab, size=12, anchor="end", color=col)
        c.rect(175, y, 280, 26, rx=3, sop=0.3)
        c.rect(175, y, 280 * v, 26, rx=3, stroke=col, fill=col, op=0.15)
        c.text(465, y + 17, f"{int(v*100)}%", size=12, color=col)
    c.text(300, 250, "≠ votre cas d'usage réel", size=11, anchor="middle", op=0.6)


# ── Impact environnemental ──────────────────────────────────────────────
@rec("empreinte-carbone",
     "Chaque requête a une empreinte carbone qui dépend du mix électrique.",
     "Each request has a carbon footprint that depends on the electricity mix.")
def _(c):
    c.eyebrow("empreinte carbone")
    c.path("M 180 210 A 90 90 0 0 1 360 210", stroke=INK, sw=2)
    import math
    for i in range(6):
        a = math.pi - i * math.pi / 5
        x1, y1 = 270 + 90 * math.cos(a), 210 - 90 * math.sin(a)
        x2, y2 = 270 + 78 * math.cos(a), 210 - 78 * math.sin(a)
        c.line(x1, y1, x2, y2, sw=1.5, op=0.6)
    a = math.pi - 0.8 * math.pi
    c.line(270, 210, 270 + 70 * math.cos(a), 210 - 70 * math.sin(a), stroke=POS, sw=2.5, arrow=True)
    c.circle(270, 210, 5, fill=INK, stroke="none")
    c.text(210, 200, "FR", size=11, color=POS)
    c.text(345, 200, "US", size=11, color=INK)
    c.text(430, 160, "×5 à ×10\nselon le mix", size=12, anchor="middle", op=0.7)


@rec("sobriete-numerique",
     "Sobriété numérique : choisir le modèle minimal qui suffit à la tâche.",
     "Digital sobriety: choosing the minimal model that suffices for the task.")
def _(c):
    c.eyebrow("sobriété numérique")
    c.node(90, 110, 150, 100, "GRAND\nMODÈLE", size=13, dash="5 4")
    c.text(165, 235, "coûteux", size=11, anchor="middle", op=0.5)
    c.cross(230, 120, INK, 8)
    c.text(300, 160, "→", size=24, anchor="middle")
    c.node(360, 135, 100, 55, "PETIT\nMODÈLE", size=12, color=POS)
    c.check(400, 200, POS, 1.3)
    c.text(410, 235, "suffit souvent", size=11, anchor="middle", color=POS, op=0.8)


# ── Prompting & usage ───────────────────────────────────────────────────
@rec("prompt-injection",
     "Injection de prompt : une instruction malveillante cachée détourne le modèle.",
     "Prompt injection: a hidden malicious instruction hijacks the model.")
def _(c):
    c.eyebrow("injection de prompt")
    c.node(80, 120, 150, 80, "DOCUMENT", size=12)
    c.text(155, 165, "...texte normal...", size=10, anchor="middle", op=0.4)
    c.text(155, 185, "[ordre caché]", size=10, anchor="middle", color=INK)
    c.line(230, 160, 275, 160, arrow=True)
    c.node(285, 125, 110, 70, "AGENT", size=14)
    c.line(395, 160, 440, 160, arrow=True)
    c.node(450, 130, 100, 60, "action\ndétournée", size=11, dash="4 4")
    c.text(300, 240, "les données peuvent porter des instructions", size=10, anchor="middle", op=0.5)


@rec("guardrails",
     "Garde-fous : des filtres encadrent les entrées et sorties d'un modèle.",
     "Guardrails: filters frame a model's inputs and outputs.")
def _(c):
    c.eyebrow("garde-fous")
    c.line(150, 80, 150, 250, stroke=INK, sw=3, dash="10 6")
    c.line(450, 80, 450, 250, stroke=INK, sw=3, dash="10 6")
    c.node(240, 130, 120, 70, "MODÈLE", size=14)
    c.line(70, 165, 145, 165, arrow=True)
    c.text(105, 150, "entrée", size=10, anchor="middle", op=0.6)
    c.line(455, 165, 530, 165, arrow=True)
    c.text(495, 150, "sortie", size=10, anchor="middle", op=0.6)
    c.text(150, 270, "filtre", size=10, anchor="middle", color=POS)
    c.text(450, 270, "filtre", size=10, anchor="middle", color=POS)


# ── Données ─────────────────────────────────────────────────────────────
@rec("lock-in",
     "Verrouillage fournisseur : plus le temps passe, plus il devient coûteux de changer.",
     "Vendor lock-in: the more time passes, the costlier it becomes to switch.")
def _(c):
    c.eyebrow("dépendance fournisseur")
    c.node(120, 120, 130, 70, "FOURNISSEUR", size=11)
    c.path("M 250 145 a 22 22 0 0 1 60 0 l 0 20 l -60 0 z", stroke=INK, sw=2, sop=0)
    c.rect(255, 150, 60, 45, rx=5)
    c.path("M 262 150 a 12 12 0 0 1 24 0", stroke=INK, sw=2, fill="none")
    c.circle(285, 172, 5, fill=INK, stroke="none")
    c.text(430, 145, "switching time", size=11, anchor="middle", op=0.7)
    c.text(430, 165, "> 6 mois", size=13, anchor="middle", color=INK)
    c.text(300, 245, "mesurez votre coût de sortie", size=11, anchor="middle", op=0.6)


@rec("roi-ia",
     "ROI de l'IA : mesurer la valeur réelle créée face au coût total.",
     "AI ROI: measuring the real value created against the total cost.")
def _(c):
    c.eyebrow("retour sur investissement")
    c.line(110, 240, 500, 240, arrow=True, sop=0.5)
    c.line(110, 240, 110, 80, arrow=True, sop=0.5)
    c.path("M 110 220 C 200 215 260 120 470 90", stroke=POS, sw=2.5)
    c.path("M 110 225 L 470 200", stroke=INK, sw=2, dash="5 4")
    c.text(480, 90, "valeur", size=11, color=POS)
    c.text(480, 200, "coût", size=11, color=INK)
    c.text(300, 270, "ce qui ne se mesure pas ne se pilote pas", size=10,
           anchor="middle", op=0.5)


@rec("mistral-ai",
     "Mistral AI : acteur français publiant des modèles ouverts, alternative souveraine.",
     "Mistral AI: a French player releasing open models, a sovereign alternative.")
def _(c):
    c.eyebrow("mistral ai")
    c.rect(230, 100, 140, 100, rx=8)
    # vent stylisé
    for i, y in enumerate([125, 145, 165, 185]):
        c.line(250, y, 350, y, stroke=[INK, GOLD, POS, INK][i], sw=6, op=0.8)
    c.text(300, 225, "modèles ouverts · France", size=11, anchor="middle", color=POS, op=0.9)
    c.text(300, 250, "alternative à ChatGPT", size=11, anchor="middle", op=0.5)


@rec("ecosysteme-ia-francais",
     "Écosystème IA français : une chaîne complète, du modèle à l'hébergement souverain.",
     "French AI ecosystem: a complete chain, from model to sovereign hosting.")
def _(c):
    c.eyebrow("écosystème ia français")
    chain = ["MISTRAL", "OVHcloud", "INTÉGRATION"]
    for i, s in enumerate(chain):
        x = 70 + i * 180
        c.node(x, 130, 150, 60, s, size=12, color=POS if i < 2 else INK)
        if i < 2:
            c.line(x + 150, 160, x + 180, 160, arrow=True)
    c.text(300, 230, "bâtir de bout en bout sans les géants US", size=11,
           anchor="middle", op=0.6)
