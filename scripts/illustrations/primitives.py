#!/usr/bin/env python3
"""
Librairie de primitives SVG pour les illustrations conceptuelles du glossaire.

Style « blueprint / schéma technique » : fond charcoal, tracé monochrome
orange PragmaForma, police monospace, lignes fines à bouts arrondis, petits
labels. Chaque illustration est une métaphore conceptuelle du terme, composée
à partir de ces primitives (originales, aux couleurs PragmaForma).

Palette (charte PragmaForma) :
  BG    fond charcoal
  INK   orange signature (tracé et texte principaux)
  POS   vert (états « validés / positifs »)
  DIM   cream discret (labels secondaires)
"""

import html

BG = "#1a1b1c"
INK = "#F65009"
POS = "#4a8d76"
DIM = "#b8b2a6"
GOLD = "#c9a671"


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


class Canvas:
    def __init__(self, w: int = 600, h: int = 300):
        self.w, self.h = w, h
        self.body: list[str] = []

    # ── base ────────────────────────────────────────────────────────────
    def raw(self, s: str):
        self.body.append(s)
        return self

    def rect(self, x, y, w, h, rx=0, fill="none", stroke=INK, sw=2, dash=None, op=1, sop=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'fill-opacity="{op}" stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{sop}"{d}/>'
        )
        return self

    def line(self, x1, y1, x2, y2, stroke=INK, sw=2, dash=None, op=1, cap="round", arrow=False, sop=None):
        if sop is not None:
            op = sop
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#a)"' if arrow else ""
        self.body.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="{cap}" stroke-opacity="{op}"{d}{m}/>'
        )
        return self

    def path(self, d, fill="none", stroke=INK, sw=2, op=1, sop=1, dash=None, arrow=False):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#a)"' if arrow else ""
        self.body.append(
            f'<path d="{d}" fill="{fill}" fill-opacity="{op}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-opacity="{sop}" stroke-linecap="round" '
            f'stroke-linejoin="round"{da}{m}/>'
        )
        return self

    def circle(self, cx, cy, r, fill="none", stroke=INK, sw=2, op=1, sop=1, dash=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" fill-opacity="{op}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{sop}"{da}/>'
        )
        return self

    def text(self, x, y, s, size=14, color=INK, anchor="start", op=1, bold=False,
             italic=False, spacing=0, rot=None):
        w = ' font-weight="bold"' if bold else ""
        it = ' font-style="italic"' if italic else ""
        ls = f' letter-spacing="{spacing}"' if spacing else ""
        tr = f' transform="rotate({rot} {x},{y})"' if rot is not None else ""
        self.body.append(
            f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" '
            f'fill="{color}" fill-opacity="{op}" text-anchor="{anchor}"{w}{it}{ls}{tr}>{esc(s)}</text>'
        )
        return self

    # ── composites courants ─────────────────────────────────────────────
    def eyebrow(self, s):
        """Titre en capitales, centré en haut, façon en-tête de schéma."""
        return self.text(self.w / 2, 40, s.upper(), size=13, anchor="middle",
                         spacing=3, op=0.9)

    def node(self, x, y, w, h, label="", color=INK, filled=False, dash=None, size=13,
             sub=None):
        """Boîte étiquetée."""
        self.rect(x, y, w, h, rx=5, stroke=color,
                  fill=color if filled else "none",
                  op=0.12 if filled else 1, dash=dash)
        if label:
            self.text(x + w / 2, y + h / 2 + (0 if not sub else -6) + 5, label,
                      size=size, color=color, anchor="middle")
        if sub:
            self.text(x + w / 2, y + h / 2 + 15, sub, size=11, color=color,
                      anchor="middle", op=0.6)
        return self

    def track(self, x, y, w, pct, color=INK, label=None):
        """Barre de progression façon terminal."""
        self.line(x, y, x + w, y, stroke=color, sw=10, dash="6 2", op=0.2)
        self.line(x, y, x + w * pct, y, stroke=color, sw=10, dash="6 2")
        self.rect(x - 4, y - 8, w + 8, 16, rx=3, stroke=color, sw=1.5)
        if label:
            self.text(x + w + 16, y + 4, label, size=12, color=color)
        return self

    def cursor(self, x, y, color=INK, h=16):
        self.body.append(
            f'<rect x="{x}" y="{y}" width="8" height="{h}" fill="{color}">'
            f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" '
            f'repeatCount="indefinite"/></rect>'
        )
        return self

    def dots(self, x, y, n=3, color=INK, r=2, gap=8):
        for i in range(n):
            self.circle(x + i * gap, y, r, fill=color, stroke="none",
                        op=1 - i * (0.8 / max(n - 1, 1)))
        return self

    def check(self, x, y, color=POS, s=1.0):
        self.path(f"M {x} {y} l {4*s} {4*s} l {8*s} {-9*s}", stroke=color, sw=2.2)
        return self

    def cross(self, x, y, color=INK, s=5):
        self.line(x - s, y - s, x + s, y + s, stroke=color, sw=2)
        self.line(x + s, y - s, x - s, y + s, stroke=color, sw=2)
        return self

    def brace(self, x, y1, y2, color=INK, label=None, side="right"):
        my = (y1 + y2) / 2
        d = 8 if side == "right" else -8
        self.path(f"M {x} {y1} q {d} 0 {d} 10 L {x+d} {my-6} q 0 6 {d} 6 "
                  f"q {-d} 0 {-d} 6 L {x+d} {y2-10} q 0 10 {-d} 10",
                  stroke=color, sw=1.6)
        if label:
            self.text(x + d + (10 if side == "right" else -10), my + 4, label,
                      size=12, color=color, anchor="start" if side == "right" else "end")
        return self

    def grid(self, x, y, w, h, step=20, color=INK, op=0.08):
        gx = x
        while gx <= x + w:
            self.line(gx, y, gx, y + h, stroke=color, sw=1, op=op)
            gx += step
        gy = y
        while gy <= y + h:
            self.line(x, gy, x + w, gy, stroke=color, sw=1, op=op)
            gy += step
        return self

    def render(self) -> str:
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
            f'role="img">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>'
            f'<rect width="{self.w}" height="{self.h}" fill="{BG}"/>'
            + "".join(self.body)
            + "</svg>"
        )
