#!/usr/bin/env python3
"""
Migration des 80 fiches du glossaire PragmaForma existant vers les
Content Collections Astro (un JSON par terme).

Source : sources/glossaire-snapshot-2026-07-10.html (copie figée de
https://pragmaforma.com/glossaire.html).

Règles validées par le commanditaire :
 · texte préservé à l'identique, SAUF normalisation des tirets cadratins
   (— remplacé par · conformément à la charte) ;
 · ajout des champs slug / theme / terme_en curés (table MAPPING ci-dessous) ;
 · statut = a_relire pour toutes les fiches migrées.

Sortie : src/content/termes/<slug>.json + rapport de migration sur stdout.
"""

import html
import json
import re
import sys
import unicodedata
from pathlib import Path


def norm_key(s: str) -> str:
    """Clé de comparaison : minuscules, sans accents, tirets → espaces."""
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[-_/]", " ", s)
    s = re.sub(r"\b(de|des|du|d|la|le|les|l)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "sources" / "glossaire-snapshot-2026-07-10.html"
OUT = ROOT / "src" / "content" / "termes"

AXES = {"fond": "fondamentaux", "resp": "responsabilite", "souv": "souverainete",
        "reg": "reglementaire", "eco": "economie"}
NIVEAUX = {"fondamental": "fondamental", "intermediaire": "intermediaire",
           "avance": "avance"}

# Table curée : data-name → (slug, theme, terme_en)
MAPPING = {
    "ai act": ("ai-act", "cadre-juridique", "AI Act"),
    "acv analyse cycle de vie": ("acv", "impact-environnemental", "Life Cycle Assessment (LCA)"),
    "agent ia agentique": ("agent-ia", "rag-agents", "AI agent"),
    "api": ("api", "ecosysteme-outils", "API"),
    "audit documentaire": ("audit-documentaire", "donnees", "Document audit"),
    "big tech gafam": ("big-tech", "ecosysteme-outils", "Big Tech"),
    "biais algorithmique": ("biais-algorithmique", "evaluation-qualite", "Algorithmic bias"),
    "benchmark": ("benchmark", "evaluation-qualite", "Benchmark"),
    "cloud act": ("cloud-act", "cadre-juridique", "CLOUD Act"),
    "charte ia": ("charte-ia", "cadre-juridique", "AI charter"),
    "chatgpt": ("chatgpt", "ecosysteme-outils", "ChatGPT"),
    "chatbot": ("chatbot", "prompting-usage", "Chatbot"),
    "claude anthropic": ("claude", "ecosysteme-outils", "Claude"),
    "cloud souverain": ("cloud-souverain", "ecosysteme-outils", "Sovereign cloud"),
    "copilot microsoft": ("copilot", "ecosysteme-outils", "Copilot"),
    "coaching pragmaforma": ("coaching-pragmaforma", "ecosysteme-outils", "PragmaForma coaching"),
    "cpf compte personnel formation": ("cpf", "cadre-juridique", "CPF (French personal training account)"),
    "communaute pragmaforma": ("communaute-pragmaforma", "ecosysteme-outils", "PragmaForma community"),
    "data center centre de donnees": ("data-center", "impact-environnemental", "Data center"),
    "dax data analysis expressions": ("dax", "ecosysteme-outils", "DAX (Data Analysis Expressions)"),
    "deploiement ia": ("deploiement-ia", "ecosysteme-outils", "AI deployment"),
    "distillation": ("distillation", "entrainement-apprentissage", "Distillation"),
    "dsi": ("dsi", "ecosysteme-outils", "CIO / IT department"),
    "ecologits": ("ecologits", "impact-environnemental", "EcoLogits"),
    "embedding plongement": ("embedding", "architecture-modeles", "Embedding"),
    "empreinte carbone": ("empreinte-carbone", "impact-environnemental", "Carbon footprint"),
    "entrainement training": ("entrainement", "entrainement-apprentissage", "Training"),
    "ethique ia": ("ethique-ia", "cadre-juridique", "AI ethics"),
    "evaluation llm eval": ("evaluation-llm", "evaluation-qualite", "LLM evaluation"),
    "fenetre contextuelle context window": ("fenetre-contextuelle", "architecture-modeles", "Context window"),
    "fine tuning": ("fine-tuning", "entrainement-apprentissage", "Fine-tuning"),
    "federated learning apprentissage federe": ("federated-learning", "entrainement-apprentissage", "Federated learning"),
    "gemini google": ("gemini", "ecosysteme-outils", "Gemini"),
    "guardrails garde fous": ("guardrails", "securite", "Guardrails"),
    "gouvernance ia": ("gouvernance-ia", "cadre-juridique", "AI governance"),
    "ia generative": ("ia-generative", "architecture-modeles", "Generative AI"),
    "ia non generative": ("ia-non-generative", "architecture-modeles", "Non-generative AI"),
    "gpu": ("gpu", "architecture-modeles", "GPU"),
    "hallucination": ("hallucination", "evaluation-qualite", "Hallucination"),
    "hebergement delegue": ("hebergement-delegue", "ecosysteme-outils", "Managed hosting"),
    "hugging face": ("hugging-face", "ecosysteme-outils", "Hugging Face"),
    "ia souveraine": ("ia-souveraine", "ecosysteme-outils", "Sovereign AI"),
    "inference": ("inference", "architecture-modeles", "Inference"),
    "jury certification": ("jury-certification", "ecosysteme-outils", "Certification jury"),
    "llama meta": ("llama", "ecosysteme-outils", "Llama"),
    "langchain orchestration": ("langchain", "rag-agents", "LangChain"),
    "llm large language model": ("llm", "architecture-modeles", "Large Language Model (LLM)"),
    "lock in dependance": ("lock-in", "ecosysteme-outils", "Vendor lock-in"),
    "mistral ai": ("mistral-ai", "ecosysteme-outils", "Mistral AI"),
    "multimodal": ("multimodal", "architecture-modeles", "Multimodal"),
    "modeles diffusion": ("modeles-diffusion", "architecture-modeles", "Diffusion models"),
    "modeles symboliques": ("modeles-symboliques", "architecture-modeles", "Symbolic AI"),
    "monitoring observabilite": ("monitoring", "evaluation-qualite", "Monitoring & observability"),
    "mooc": ("mooc", "ecosysteme-outils", "MOOC"),
    "open source ia": ("open-source-ia", "ecosysteme-outils", "Open-source AI"),
    "openrag": ("openrag", "rag-agents", "OpenRAG"),
    "ori ia": ("ori-ia", "ecosysteme-outils", "ORI-IA workshop"),
    "outils proprietaires": ("outils-proprietaires", "ecosysteme-outils", "Proprietary tools"),
    "power bi": ("power-bi", "ecosysteme-outils", "Power BI"),
    "prompt prompting": ("prompt", "prompting-usage", "Prompt"),
    "prompt injection": ("prompt-injection", "securite", "Prompt injection"),
    "pue power usage effectiveness": ("pue", "impact-environnemental", "PUE (Power Usage Effectiveness)"),
    "rag retrieval augmented generation": ("rag", "rag-agents", "RAG (Retrieval-Augmented Generation)"),
    "rgpd gdpr": ("rgpd", "cadre-juridique", "GDPR"),
    "rlhf reinforcement learning human feedback": ("rlhf", "entrainement-apprentissage", "RLHF"),
    "droits auteur ia": ("droits-auteur-ia", "cadre-juridique", "AI & copyright"),
    "securite donnees": ("securite-donnees", "securite", "Data security"),
    "sobriete numerique": ("sobriete-numerique", "impact-environnemental", "Digital sobriety"),
    "souverainete numerique": ("souverainete-numerique", "cadre-juridique", "Digital sovereignty"),
    "synchrone asynchrone": ("synchrone-asynchrone", "ecosysteme-outils", "Synchronous / asynchronous"),
    "scraping web data": ("scraping", "donnees", "Web scraping"),
    "tco total cost ownership": ("tco", "ecosysteme-outils", "TCO (Total Cost of Ownership)"),
    "test validation ia": ("test-validation-ia", "evaluation-qualite", "AI testing & validation"),
    "temperature": ("temperature", "prompting-usage", "Temperature"),
    "token tokenisation": ("token", "architecture-modeles", "Token"),
    "transformer": ("transformer", "architecture-modeles", "Transformer"),
    "vector store base vectorielle": ("vector-store", "rag-agents", "Vector store"),
    "vibe coding": ("vibe-coding", "prompting-usage", "Vibe coding"),
    "webinaire": ("webinaire", "ecosysteme-outils", "Webinar"),
    "zero shot few shot": ("zero-shot-few-shot", "prompting-usage", "Zero-shot / few-shot"),
}


def clean(text: str) -> str:
    """Désentitise, compacte les blancs et normalise les cadratins (charte)."""
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    # Charte PragmaForma : pas de tiret cadratin · point médian à la place.
    text = re.sub(r"\s*—\s*", " · ", text)
    return text


def strip_tags(fragment: str) -> str:
    return clean(re.sub(r"<[^>]+>", " ", fragment))


def first(pattern: str, text: str, flags=re.S) -> str:
    m = re.search(pattern, text, flags)
    return m.group(1) if m else ""


def parse_article(art: str) -> dict:
    head = first(r'<div class="term-head">(.*?)</div>\s*<div class="term-body">', art)
    body = first(r'<div class="term-body">(.*?)$', art)

    data_axis = first(r'data-axis="(\w+)"', art)
    data_level = first(r'data-level="(\w+)"', art)
    data_page = first(r'data-page="([^"]*)"', art)
    data_name = first(r'data-name="([^"]+)"', art)

    terme_fr = strip_tags(first(r"<h3>(.*?)</h3>", head))
    aka = strip_tags(first(r'<p class="term-aka">(.*?)</p>', head))

    # Définition = premier <p> direct du corps (avant le bloc exemple)
    definition = strip_tags(first(r"^\s*<p>(.*?)</p>", body))
    exemple = strip_tags(
        first(r'<div class="example-label">.*?</div>\s*<p>(.*?)</p>', body)
    )
    regard = strip_tags(
        first(r'<div class="pragma-note-label">.*?</div>\s*<p>(.*?)</p>', body)
    )

    # Bloc « page liée » : soit un CTA vers une page du site, soit un « Voir aussi »
    cta = None
    termes_lies_noms = []
    rp = re.search(
        r'<a href="([^"]*)" class="related-page">.*?'
        r'<span class="related-page-text">(.*?)</span>.*?'
        r'<span class="related-page-link">(.*?)</span>',
        body,
        re.S,
    )
    if rp:
        rp_url, rp_text, rp_label = rp.group(1), strip_tags(rp.group(2)), strip_tags(rp.group(3))
        m = re.match(r"Voir aussi(?:\s+les termes liés)?\s*:\s*(.+)", rp_text)
        if m:
            termes_lies_noms = [n.strip() for n in m.group(1).split(",") if n.strip()]
        else:
            cta = {
                "texte_fr": rp_text,
                "texte_en": "",
                "label_fr": rp_label,
                "label_en": "",
                "url": rp_url,
            }

    # Sources : liens du bloc .source, sinon texte brut après « Source : »
    sources = []
    src_block = first(r'<div class="source">(.*?)</div>', body)
    if src_block:
        for m in re.finditer(r'<a href="([^"]+)"[^>]*>(.*?)</a>', src_block, re.S):
            url = html.unescape(m.group(1))
            if url.startswith("/"):
                url = "https://pragmaforma.com" + url
            sources.append({"titre": strip_tags(m.group(2)), "url": url})
        if not sources:
            txt = strip_tags(src_block)
            txt = re.sub(r"^Source\s*:\s*", "", txt)
            if txt:
                sources.append({"titre": txt})

    return {
        "data_name": data_name,
        "axe": AXES[data_axis],
        "niveau": NIVEAUX[data_level],
        "pages_liees": data_page.split() if data_page else [],
        "terme_fr": terme_fr,
        "sous_titre_fr": aka,
        "definition_fr": definition,
        "exemple_fr": exemple,
        "regard_fr": regard,
        "cta": cta,
        "sources": sources,
        "_termes_lies_noms": termes_lies_noms,
    }


def main() -> int:
    html_doc = SRC.read_text(encoding="utf-8")
    articles = re.findall(r'<article class="term".*?</article>', html_doc, re.S)
    if len(articles) != 80:
        print(f"ERREUR : {len(articles)} articles trouvés, 80 attendus", file=sys.stderr)
        return 1

    parsed = [parse_article(a) for a in articles]

    # Index nom → slug pour résoudre les « Voir aussi »
    # (nom du terme + composantes du data-name + sous-titre)
    name_to_slug = {}
    for p in parsed:
        slug, _, _ = MAPPING[p["data_name"]]
        name_to_slug[norm_key(p["terme_fr"])] = slug
        name_to_slug[norm_key(p["data_name"])] = slug
        name_to_slug[norm_key(slug)] = slug
    # Composantes des data-name en repli (après les noms complets,
    # pour ne pas écraser une clé exacte)
    for p in parsed:
        slug, _, _ = MAPPING[p["data_name"]]
        for token in norm_key(p["data_name"]).split():
            if len(token) > 2:
                name_to_slug.setdefault(token, slug)

    OUT.mkdir(parents=True, exist_ok=True)
    unresolved = []
    skipped = []
    report = {"files": 0, "with_cta": 0, "with_sources": 0, "with_lies": 0, "emdash": 0}

    for p in parsed:
        slug, theme, terme_en = MAPPING[p["data_name"]]

        # Ne jamais écraser une fiche déjà enrichie (schéma, vidéo, articles
        # ou traduction EN présents) : la migration ne régénère que le brut.
        target = OUT / f"{slug}.json"
        if target.exists():
            existing = json.loads(target.read_text(encoding="utf-8"))
            if (
                existing.get("schema", {}).get("type") != "none"
                or existing.get("video")
                or existing.get("articles")
                or existing.get("definition_en")
            ):
                skipped.append(slug)
                continue

        lies = []
        for nom in p.pop("_termes_lies_noms"):
            key = norm_key(nom)
            found = name_to_slug.get(key)
            if not found:
                # tentative : correspondance partielle sur les noms de termes
                for cand_name, cand_slug in name_to_slug.items():
                    if key in cand_name or cand_name in key:
                        found = cand_slug
                        break
            if found and found != slug:
                lies.append(found)
            elif not found:
                unresolved.append((slug, nom))

        record = {
            "terme_fr": p["terme_fr"],
            "terme_en": terme_en,
            "sous_titre_fr": p["sous_titre_fr"],
            "sous_titre_en": "",
            "axe": p["axe"],
            "niveau": p["niveau"],
            "theme": theme,
            "pages_liees": p["pages_liees"],
            "definition_fr": p["definition_fr"],
            "definition_en": "",
            "exemple_fr": p["exemple_fr"],
            "exemple_en": "",
            "regard_fr": p["regard_fr"],
            "regard_en": "",
            "schema": {"type": "none", "contenu": "", "alt_fr": "", "alt_en": ""},
            "video": None,
            "articles": [],
            "termes_lies": sorted(set(lies)),
            "sources": p["sources"],
            "cta": p["cta"],
            "statut": "a_relire",
        }

        for field in ("definition_fr", "exemple_fr", "regard_fr"):
            if "—" in record[field]:
                report["emdash"] += 1
        if not record["definition_fr"]:
            print(f"ATTENTION : définition vide pour {slug}", file=sys.stderr)

        target.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        report["files"] += 1
        report["with_cta"] += 1 if record["cta"] else 0
        report["with_sources"] += 1 if record["sources"] else 0
        report["with_lies"] += 1 if record["termes_lies"] else 0

    if skipped:
        print(f"Fiches enrichies préservées : {len(skipped)} ({', '.join(skipped)})")
    print(f"Fiches écrites      : {report['files']}")
    print(f"Avec CTA            : {report['with_cta']}")
    print(f"Avec sources        : {report['with_sources']}")
    print(f"Avec termes liés    : {report['with_lies']}")
    print(f"Cadratins restants  : {report['emdash']}")
    if unresolved:
        print("\nTermes liés NON résolus (à corriger à la main) :")
        for slug, nom in unresolved:
            print(f"  {slug} → « {nom} »")
    return 0


if __name__ == "__main__":
    sys.exit(main())
