"""Generate the SVG assets used by the profile README.

Standard library only. Run from the repository root:

    python scripts/generate_assets.py

Edit the PROJECTS list below to change card content, then re-run.
All SVGs are self-contained (no external fonts, images or scripts), so
GitHub renders them reliably through its image proxy.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "'Segoe UI', 'Helvetica Neue', Ubuntu, Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"

# Palette
BG_0 = "#050912"
BG_1 = "#0B1530"
CARD = "#0A1122"
BORDER = "#1C2A47"
TEXT = "#E6EDF7"
MUTED = "#8B9BB4"
CYAN = "#22D3EE"
BLUE = "#3B82F6"


def banner() -> str:
    w, h = 1280, 320
    # Static node graph on the right side (abstract model / agent graph).
    nodes = [
        (900, 70), (1000, 120), (1110, 70), (1200, 140),
        (880, 190), (990, 230), (1100, 190), (1210, 250),
        (1060, 280), (940, 280),
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (0, 4), (1, 4), (1, 5), (1, 6), (2, 6),
        (3, 6), (3, 7), (4, 5), (5, 6), (6, 7), (5, 8), (6, 8), (4, 9),
        (5, 9), (8, 7),
    ]
    lines = "\n".join(
        f'    <line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" '
        f'y2="{nodes[b][1]}" />'
        for a, b in edges
    )
    circles = "\n".join(
        f'    <circle cx="{x}" cy="{y}" r="{7 if i in (1, 6) else 4.5}" '
        f'fill="{CYAN if i in (1, 6) else BLUE}" '
        f'opacity="{0.95 if i in (1, 6) else 0.75}" />'
        for i, (x, y) in enumerate(nodes)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
  <title id="t">Zakaria Ould Miloud</title>
  <desc id="d">AI Engineer, LLM Engineer, Agentic AI Developer and Full-Stack Developer.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{BG_0}" />
      <stop offset="1" stop-color="{BG_1}" />
    </linearGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}" />
      <stop offset="1" stop-color="{BLUE}" />
    </linearGradient>
    <radialGradient id="glow" cx="0.8" cy="0.5" r="0.45">
      <stop offset="0" stop-color="{BLUE}" stop-opacity="0.22" />
      <stop offset="1" stop-color="{BLUE}" stop-opacity="0" />
    </radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#13213F" stroke-width="1" />
    </pattern>
  </defs>
  <rect width="{w}" height="{h}" rx="18" fill="url(#bg)" />
  <rect width="{w}" height="{h}" rx="18" fill="url(#grid)" opacity="0.55" />
  <rect width="{w}" height="{h}" rx="18" fill="url(#glow)" />
  <g stroke="{BLUE}" stroke-opacity="0.35" stroke-width="1.4">
{lines}
  </g>
  <g>
{circles}
  </g>
  <text x="72" y="92" font-family="{MONO}" font-size="16" letter-spacing="3" fill="{CYAN}">AI ENGINEERING  /  LANGUAGE TECHNOLOGY</text>
  <text x="70" y="158" font-family="{FONT}" font-size="56" font-weight="700" fill="{TEXT}">Zakaria Ould Miloud</text>
  <rect x="72" y="180" width="96" height="4" rx="2" fill="url(#accent)" />
  <text x="72" y="222" font-family="{FONT}" font-size="23" fill="{TEXT}">AI Engineer  ·  LLM Engineer  ·  Agentic AI  ·  Full-Stack</text>
  <text x="72" y="258" font-family="{FONT}" font-size="17" fill="{MUTED}">Arabic NLP and Algerian Darija  ·  Dataset engineering  ·  RAG  ·  Local AI</text>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="18" fill="none" stroke="{BORDER}" />
</svg>
"""


PROJECTS = [
    {
        "slug": "tassili",
        "title": "Tassili.ai",
        "subtitle": "Language models for Algerian Darija",
        "tag": "COMPANY · PRIVATE",
        "bullets": [
            "Darija data collection and web scraping",
            "Cleaning, deduplication and dataset audits",
            "Tokenization and SFT data preparation",
            "LLM / SLM training on the Hugging Face stack",
        ],
        "chips": ["Python", "Hugging Face", "NLP", "LLM / SLM"],
    },
    {
        "slug": "dzinsight",
        "title": "DzInsight",
        "subtitle": "Social media intelligence for Algerian content",
        "tag": "M.SC. CAPSTONE · PRIVATE",
        "bullets": [
            "TikTok, Instagram, YouTube, Facebook, Telegram",
            "Darija speech-to-text with a Darija Whisper model",
            "Sentiment: DziriBERT, CAMeLBERT, XLM-R",
            "Vision: YOLO, DeepFace, EasyOCR",
            "RAG chat: embeddings + BM25, LLM via Groq / Ollama",
        ],
        "chips": ["FastAPI", "React", "SQLite", "faster-whisper"],
    },
    {
        "slug": "najda",
        "title": "NAJDA",
        "subtitle": "Road-crash emergency decision support",
        "tag": "SOLVEX 3.0 · PRIVATE",
        "bullets": [
            "Mobile crash report to a live dispatcher queue",
            "Geospatial data with PostGIS, live map over WebSocket",
            "Human in the loop: it suggests, the dispatcher decides",
            "Shared TS / Python test vectors, CI and auto-deploy",
        ],
        "chips": ["FastAPI", "PostGIS", "React", "Expo"],
    },
    {
        "slug": "search-agent",
        "title": "Search AI Agent",
        "subtitle": "ReAct web-search agent with LangChain",
        "tag": "OPEN SOURCE",
        "bullets": [
            "ReAct loop: reason, call a tool, observe, answer",
            "Tavily web search tool (top 3 results)",
            "Groq-hosted LLM at temperature 0",
            "Streamlit chat UI with session history",
        ],
        "chips": ["LangChain", "Groq", "Tavily", "Streamlit"],
    },
    {
        "slug": "code-reviewer",
        "title": "AI Code Reviewer",
        "subtitle": "LLM code review with structured JSON output",
        "tag": "OPEN SOURCE",
        "bullets": [
            "Finds bugs, security and performance issues",
            "Findings ranked by severity, 0–100 quality score",
            "Demo mode works without an API key",
            "Serverless deployment config for Vercel",
        ],
        "chips": ["FastAPI", "Groq", "Llama 3.3 70B", "Vanilla JS"],
    },
    {
        "slug": "env-monitor",
        "title": "Smart Environmental Monitor",
        "subtitle": "Real-time anomaly detection on sensor streams",
        "tag": "OPEN SOURCE",
        "bullets": [
            "Simulated sensor: temperature, humidity, air quality",
            "Isolation Forest scores every reading live",
            "WebSocket broadcast to all open dashboards",
            "Dependency-free canvas dashboard",
        ],
        "chips": ["FastAPI", "scikit-learn", "WebSockets", "NumPy"],
    },
]


def _chip_width(label: str) -> int:
    # Rough width estimate for 13px text, plus padding.
    return int(len(label) * 7.4) + 24


def card(p: dict) -> str:
    w, h = 520, 300
    tag = escape(p["tag"])
    tag_w = int(len(p["tag"]) * 7.2) + 22
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">',
        f'  <title id="t">{escape(p["title"])}: {escape(p["subtitle"])}</title>',
        "  <defs>",
        '    <linearGradient id="a" x1="0" y1="0" x2="1" y2="0">',
        f'      <stop offset="0" stop-color="{CYAN}" />',
        f'      <stop offset="1" stop-color="{BLUE}" />',
        "    </linearGradient>",
        "  </defs>",
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" '
        f'fill="{CARD}" stroke="{BORDER}" />',
        f'  <rect x="24" y="0.5" width="64" height="3" rx="1.5" fill="url(#a)" />',
        f'  <text x="24" y="50" font-family="{FONT}" font-size="24" '
        f'font-weight="700" fill="{TEXT}">{escape(p["title"])}</text>',
        f'  <rect x="{w - 24 - tag_w}" y="30" width="{tag_w}" height="24" rx="12" '
        f'fill="none" stroke="{CYAN}" stroke-opacity="0.5" />',
        f'  <text x="{w - 24 - tag_w / 2}" y="46.5" text-anchor="middle" '
        f'font-family="{MONO}" font-size="11" letter-spacing="0.5" '
        f'fill="{CYAN}">{tag}</text>',
        f'  <text x="24" y="78" font-family="{FONT}" font-size="15" '
        f'fill="{MUTED}">{escape(p["subtitle"])}</text>',
    ]
    y = 114
    step = 25 if len(p["bullets"]) > 4 else 28
    for b in p["bullets"]:
        parts.append(
            f'  <rect x="26" y="{y - 9}" width="6" height="6" rx="1" fill="{CYAN}" />'
        )
        parts.append(
            f'  <text x="42" y="{y}" font-family="{FONT}" font-size="14.5" '
            f'fill="{TEXT}">{escape(b)}</text>'
        )
        y += step
    x = 24
    cy = h - 50
    for c in p["chips"]:
        cw = _chip_width(c)
        parts.append(
            f'  <rect x="{x}" y="{cy}" width="{cw}" height="26" rx="6" '
            f'fill="#0F1C38" stroke="{BORDER}" />'
        )
        parts.append(
            f'  <text x="{x + cw / 2}" y="{cy + 17.5}" text-anchor="middle" '
            f'font-family="{MONO}" font-size="12.5" fill="#B9C7DD">{escape(c)}</text>'
        )
        x += cw + 8
    parts.append("</svg>\n")
    return "\n".join(parts)


def divider() -> str:
    w = 1280
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="8" viewBox="0 0 {w} 8" role="presentation">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0" />
      <stop offset="0.5" stop-color="{BLUE}" stop-opacity="0.9" />
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect y="3" width="{w}" height="2" rx="1" fill="url(#g)" />
</svg>
"""


def main() -> None:
    (ASSETS / "projects").mkdir(parents=True, exist_ok=True)
    (ASSETS / "banner.svg").write_text(banner(), encoding="utf-8")
    (ASSETS / "divider.svg").write_text(divider(), encoding="utf-8")
    for p in PROJECTS:
        (ASSETS / "projects" / f"{p['slug']}.svg").write_text(card(p), encoding="utf-8")
    print(f"Wrote banner, divider and {len(PROJECTS)} project cards to {ASSETS}")


if __name__ == "__main__":
    main()
