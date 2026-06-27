"""
Praxis — shared visual system.

True black, monochrome, zero border-radius, DM Sans / DM Mono.
Import inject_style() at the top of every page.
"""

import streamlit as st


# ---- token system -----------------------------------------------------

INK = "#FAFAFA"          # primary text
INK_DIM = "#8A8A8A"      # secondary text
INK_FAINT = "#4A4A4A"    # tertiary / disabled
BG = "#000000"           # page background
PANEL = "#0A0A0A"        # raised surface
LINE = "#1F1F1F"         # hairline border
LINE_BRIGHT = "#333333"  # hover border
ACCENT = "#FAFAFA"       # the only "color" — pure white, used sparingly


def inject_style():
    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">

        <style>

        :root {{
            --ink: {INK};
            --ink-dim: {INK_DIM};
            --ink-faint: {INK_FAINT};
            --bg: {BG};
            --panel: {PANEL};
            --line: {LINE};
            --line-bright: {LINE_BRIGHT};
        }}

        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif;
        }}

        .stApp {{
            background-color: var(--bg);
        }}

        /* kill streamlit chrome */
        #MainMenu, footer, header {{ visibility: hidden; }}
        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 6rem;
            max-width: 920px;
        }}

        /* every input, button, box: sharp corners, no shadow */
        * {{
            border-radius: 0px !important;
        }}

        /* ---- sidebar ---- */
        section[data-testid="stSidebar"] {{
            background-color: var(--bg);
            border-right: 1px solid var(--line);
        }}
        section[data-testid="stSidebar"] > div {{
            padding-top: 1.25rem;
        }}

        /* ---- typography helpers ---- */
        .px-eyebrow {{
            font-family: 'DM Mono', monospace;
            font-size: 11px;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: var(--ink-faint);
            margin-bottom: 4px;
        }}
        .px-mono {{
            font-family: 'DM Mono', monospace;
        }}
        .px-title {{
            font-family: 'DM Sans', sans-serif;
            font-weight: 700;
            font-size: 22px;
            color: var(--ink);
            letter-spacing: -0.01em;
            margin: 0;
        }}
        .px-sub {{
            font-family: 'DM Sans', sans-serif;
            font-size: 13px;
            color: var(--ink-dim);
            margin-top: 2px;
        }}

        /* ---- brand header (sidebar top) ---- */
        .px-brand {{
            display: flex;
            align-items: center;
            gap: 9px;
            padding: 0 4px 14px 4px;
            border-bottom: 1px solid var(--line);
            margin-bottom: 14px;
        }}
        .px-brand-mark {{
            width: 7px;
            height: 7px;
            background: var(--ink);
            flex-shrink: 0;
            animation: px-pulse 2.2s ease-in-out infinite;
        }}
        @keyframes px-pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.25; }}
        }}
        @media (prefers-reduced-motion: reduce) {{
            .px-brand-mark {{ animation: none; }}
        }}
        .px-brand-name {{
            font-family: 'DM Mono', monospace;
            font-size: 14px;
            font-weight: 500;
            letter-spacing: 0.02em;
            color: var(--ink);
        }}
        .px-brand-tag {{
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            color: var(--ink-faint);
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }}

        /* ---- nav buttons (sidebar page links) ---- */
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {{
            font-family: 'DM Sans', sans-serif;
            font-size: 14px;
            color: var(--ink-dim) !important;
            border-left: 2px solid transparent;
            padding: 7px 10px !important;
            margin-bottom: 1px;
            transition: border-color 0.15s, color 0.15s, background 0.15s;
        }}
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {{
            color: var(--ink) !important;
            background: var(--panel) !important;
            border-left-color: var(--line-bright);
        }}
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"][aria-current="page"] {{
            color: var(--ink) !important;
            border-left-color: var(--ink);
            background: var(--panel) !important;
        }}

        /* ---- panel / card ---- */
        .px-panel {{
            background: var(--panel);
            border: 1px solid var(--line);
            padding: 16px 18px;
        }}

        /* ---- buttons ---- */
        .stButton > button, .stDownloadButton > button {{
            font-family: 'DM Sans', sans-serif;
            font-size: 13px;
            font-weight: 500;
            background: transparent;
            color: var(--ink);
            border: 1px solid var(--line-bright);
            padding: 7px 16px;
            transition: background 0.15s, border-color 0.15s;
        }}
        .stButton > button:hover, .stDownloadButton > button:hover {{
            background: var(--ink);
            color: var(--bg);
            border-color: var(--ink);
        }}
        .stButton > button[kind="primary"] {{
            background: var(--ink);
            color: var(--bg);
            border-color: var(--ink);
        }}

        /* ---- inputs ---- */
        .stTextInput input, .stTextArea textarea, .stSelectbox > div > div,
        .stDateInput input, .stNumberInput input {{
            background: var(--panel) !important;
            border: 1px solid var(--line) !important;
            color: var(--ink) !important;
            font-family: 'DM Sans', sans-serif;
        }}
        .stTextInput input:focus, .stTextArea textarea:focus {{
            border-color: var(--ink-dim) !important;
        }}

        /* ---- chat ---- */
        [data-testid="stChatMessage"] {{
            background: transparent;
            border: none;
            padding: 6px 0;
        }}
        [data-testid="stChatInput"] textarea {{
            font-family: 'DM Sans', sans-serif !important;
        }}
        [data-testid="stChatInput"] {{
            background: var(--panel) !important;
            border: 1px solid var(--line) !important;
        }}

        /* ---- dataframe / table ---- */
        [data-testid="stDataFrame"] {{
            border: 1px solid var(--line) !important;
        }}

        /* ---- divider ---- */
        hr {{
            border-color: var(--line) !important;
        }}

        /* ---- status pill ---- */
        .px-pill {{
            display: inline-block;
            font-family: 'DM Mono', monospace;
            font-size: 10px;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            padding: 2px 8px;
            border: 1px solid var(--line-bright);
            color: var(--ink-dim);
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(eyebrow: str, title: str, subtitle: str = ""):
    """Consistent header block for every module page."""
    sub_html = f'<div class="px-sub">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f"""
        <div class="px-eyebrow">{eyebrow}</div>
        <div class="px-title">{title}</div>
        {sub_html}
        <div style="height:1px; background:var(--line); margin:16px 0 22px 0;"></div>
        """,
        unsafe_allow_html=True,
    )


def sidebar_brand():
    """The fixed brand block at the top of the sidebar."""
    st.markdown(
        """
        <div class="px-brand">
            <div class="px-brand-mark"></div>
            <div>
                <div class="px-brand-name">PRAXIS</div>
                <div class="px-brand-tag">AI Workspace</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -- inline SVG icon set (16x16, currentColor strokes — no emoji, ever) --

ICONS = {
    "chat": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>""",
    "todos": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>""",
    "calendar": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="18" rx="0"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>""",
    "excel": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="3" width="18" height="18" rx="0"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>""",
    "slides": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="4" width="20" height="14" rx="0"/><line x1="8" y1="22" x2="16" y2="22"/><line x1="12" y1="18" x2="12" y2="22"/></svg>""",
    "meetings": """<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>""",
}


def icon(name: str) -> str:
    return ICONS.get(name, "")