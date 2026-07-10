# -*- coding: utf-8 -*-
"""
Constructeurs de scènes de haut niveau, pour composer une illustration
conceptuelle en une ou deux lignes. Chaque fonction dessine sur un Canvas
dans le style blueprint PragmaForma.
"""
from primitives import INK, POS, DIM, GOLD, Canvas

W = 600


def _col(i, n):
    return [INK, POS, GOLD, DIM][i % 4]


def title(c: Canvas, s: str):
    c.eyebrow(s)


def flow(c: Canvas, title_s, items, caption=None, y=118, loop=False, hl=None):
    """Suite de boîtes reliées par des flèches. items: str ou (label, color)."""
    c.eyebrow(title_s)
    n = len(items)
    bw = min(140, int((W - 100 - (n - 1) * 40) / n))
    gap = 40
    total = n * bw + (n - 1) * gap
    x = (W - total) / 2
    centers = []
    for i, it in enumerate(items):
        lab, col = (it if isinstance(it, tuple) else (it, None))
        col = col or (POS if hl is not None and i == hl else INK)
        c.node(x, y, bw, 56, lab, size=12, color=col)
        centers.append((x + bw / 2, y))
        if i < n - 1:
            c.line(x + bw, y + 28, x + bw + gap, y + 28, arrow=True)
        x += bw + gap
    if loop and n >= 2:
        x0, x1 = centers[0][0], centers[-1][0]
        c.path(f"M {x1} {y+56} q 0 55 {-(x1-x0)/2} 55 q {-(x1-x0)/2} 0 {-(x1-x0)/2} -55",
               stroke=INK, sw=2, dash="5 4", arrow=True)
    if caption:
        c.text(W / 2, 250, caption, size=12, anchor="middle", op=0.6)
    return centers


def compare(c: Canvas, title_s, left, right, caption=None, winner=None):
    """Deux options côte à côte séparées par « vs ». winner: 'left'|'right'."""
    c.eyebrow(title_s)
    ll, lsub = (left if isinstance(left, tuple) else (left, None))
    rl, rsub = (right if isinstance(right, tuple) else (right, None))
    lcol = POS if winner == "left" else INK
    rcol = POS if winner == "right" else INK
    c.node(90, 115, 170, 90, ll, size=13, color=lcol, sub=lsub,
           dash="5 4" if winner == "right" else None)
    c.text(300, 165, "vs", size=18, anchor="middle", op=0.6)
    c.node(340, 115, 170, 90, rl, size=13, color=rcol, sub=rsub,
           dash="5 4" if winner == "left" else None)
    if winner == "left":
        c.check(150, 215, POS, 1.2)
    if winner == "right":
        c.check(400, 215, POS, 1.2)
    if caption:
        c.text(300, 250, caption, size=12, anchor="middle", op=0.6)


def boundary(c: Canvas, title_s, inner, caption=None, out="rien ne sort"):
    """Périmètre en pointillés contenant des nœuds : métaphore de contrôle/frontière."""
    c.eyebrow(title_s)
    c.rect(150, 80, 300, 150, rx=8, dash="8 5")
    n = len(inner)
    bw = int((280 - (n - 1) * 16) / n)
    x = 160
    for lab in inner:
        c.node(x, 120, bw, 55, lab, size=11, color=POS)
        x += bw + 16
    c.line(452, 155, 500, 155, arrow=True)
    c.cross(515, 155, INK, 7)
    c.text(300, 255, caption or out, size=12, anchor="middle", op=0.6)


def meter(c: Canvas, title_s, left_lab, right_lab, caption=None, pos=0.35):
    """Jauge en arc, aiguille positionnée entre deux extrêmes."""
    import math
    c.eyebrow(title_s)
    cx, cy, r = 300, 205, 95
    c.path(f"M {cx-r} {cy} A {r} {r} 0 0 1 {cx+r} {cy}", stroke=INK, sw=2)
    for i in range(7):
        a = math.pi - i * math.pi / 6
        c.line(cx + r * math.cos(a), cy - r * math.sin(a),
               cx + (r - 12) * math.cos(a), cy - (r - 12) * math.sin(a), sw=1.5, op=0.5)
    a = math.pi - pos * math.pi
    c.line(cx, cy, cx + (r - 22) * math.cos(a), cy - (r - 22) * math.sin(a),
           stroke=POS, sw=2.5, arrow=True)
    c.circle(cx, cy, 5, fill=INK, stroke="none")
    c.text(cx - r, cy + 22, left_lab, size=11, anchor="middle", op=0.7)
    c.text(cx + r, cy + 22, right_lab, size=11, anchor="middle", op=0.7)
    if caption:
        c.text(cx, 250, caption, size=12, anchor="middle", op=0.6)


def bars(c: Canvas, title_s, data, caption=None):
    """Barres horizontales étiquetées. data: [(label, 0..1, color?)]."""
    c.eyebrow(title_s)
    for i, row in enumerate(data):
        lab, v = row[0], row[1]
        col = row[2] if len(row) > 2 else _col(i, len(data))
        y = 95 + i * 46
        c.text(175, y + 17, lab, size=12, anchor="end", color=col)
        c.rect(190, y, 270, 26, rx=3, sop=0.3)
        c.rect(190, y, 270 * v, 26, rx=3, stroke=col, fill=col, op=0.15)
    if caption:
        c.text(300, 255, caption, size=11, anchor="middle", op=0.55)


def layers(c: Canvas, title_s, rows, caption=None):
    """Empilement de bandes (niveaux/couches). rows: [(label, color?)] du haut vers le bas."""
    c.eyebrow(title_s)
    y = 80
    for i, row in enumerate(rows):
        lab = row[0] if isinstance(row, tuple) else row
        col = row[1] if isinstance(row, tuple) and len(row) > 1 else INK
        c.rect(180, y, 240, 32, rx=4, stroke=col, fill=col, op=0.1)
        c.text(300, y + 21, lab, size=12, anchor="middle", color=col)
        y += 40
    if caption:
        c.text(300, y + 15, caption, size=11, anchor="middle", op=0.55)


def shield(c: Canvas, title_s, inner, caption=None):
    """Bouclier avec libellé central : protection/sécurité."""
    c.eyebrow(title_s)
    c.path("M 300 80 L 362 106 L 362 162 Q 362 214 300 240 Q 238 214 238 162 L 238 106 Z",
           stroke=INK, sw=2)
    c.text(300, 150, inner, size=12, anchor="middle")
    c.check(286, 168, POS, 1.2)
    if caption:
        c.text(300, 262, caption, size=11, anchor="middle", op=0.6)


def points(c: Canvas, title_s, caption=None, query=True):
    """Nuage de points dans un espace, avec requête et plus proches voisins."""
    c.eyebrow(title_s)
    c.rect(120, 75, 260, 180, rx=6, sop=0.5)
    pts = [(160, 120), (200, 210), (270, 105), (330, 175), (230, 150), (310, 235), (170, 240)]
    for x, y in pts:
        c.circle(x, y, 4, fill=INK, stroke="none", op=0.7)
    if query:
        q = (250, 165)
        c.circle(*q, 6, fill=POS, stroke="none")
        for x, y in [(270, 105), (230, 150), (330, 175)]:
            c.line(q[0], q[1], x, y, stroke=POS, sw=1.3, dash="3 3")
    c.node(420, 140, 110, 46, "TOP-K", size=13)
    c.line(382, 163, 418, 163, arrow=True)
    if caption:
        c.text(250, 275, caption, size=11, anchor="middle", op=0.55)


def beforeafter(c: Canvas, title_s, before, after, caption=None):
    """Avant → après : optimisation, transformation."""
    c.eyebrow(title_s)
    bl, bsub = (before if isinstance(before, tuple) else (before, None))
    al, asub = (after if isinstance(after, tuple) else (after, None))
    c.node(90, 120, 170, 80, bl, size=13, sub=bsub, dash="5 4")
    c.line(270, 160, 330, 160, arrow=True)
    c.node(340, 120, 170, 80, al, size=13, color=POS, sub=asub)
    if caption:
        c.text(300, 245, caption, size=12, anchor="middle", op=0.6)


def hub(c: Canvas, title_s, center, spokes, caption=None):
    """Nœud central relié à des satellites."""
    import math
    c.eyebrow(title_s)
    cx, cy = 300, 160
    c.node(cx - 60, cy - 30, 120, 60, center, size=13)
    n = len(spokes)
    for i, s in enumerate(spokes):
        a = 2 * math.pi * i / n - math.pi / 2
        x, y = cx + 165 * math.cos(a), cy + 95 * math.sin(a)
        c.line(cx + 62 * math.cos(a), cy + 34 * math.sin(a), x - 8 * math.cos(a),
               y - 6 * math.sin(a), sw=1.5, op=0.6)
        c.text(x, y + 4, s, size=11, anchor="middle", color=POS, op=0.85)
    if caption:
        c.text(cx, 275, caption, size=11, anchor="middle", op=0.55)


def brand(c: Canvas, name, tag, sub=None):
    """Carte de marque : logo textuel encadré + accroche."""
    c.eyebrow("écosystème")
    c.rect(180, 105, 240, 90, rx=8)
    c.text(300, 155, name, size=22, anchor="middle")
    if sub:
        c.text(300, 178, sub, size=11, anchor="middle", op=0.5)
    c.text(300, 225, tag, size=12, anchor="middle", color=POS, op=0.9)
