import streamlit as st
from style import inject_style, page_header, sidebar_brand, icon
from api import chat

st.set_page_config(
    page_title="Praxis — AI Workspace",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_style()

# ---- sidebar ------------------------------------------------------------
with st.sidebar:
    sidebar_brand()

    st.markdown(
        '<a href="/" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink); '
        'text-decoration:none; border-left:2px solid var(--ink); '
        'background:var(--panel); margin-bottom:1px;">Chat</a>'
        '<a href="/todos" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink-dim); '
        'text-decoration:none; border-left:2px solid transparent; margin-bottom:1px;">Todos</a>'
        '<a href="/calendar" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink-dim); '
        'text-decoration:none; border-left:2px solid transparent; margin-bottom:1px;">Calendar</a>'
        '<a href="/excel" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink-dim); '
        'text-decoration:none; border-left:2px solid transparent; margin-bottom:1px;">Excel</a>'
        '<a href="/slides" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink-dim); '
        'text-decoration:none; border-left:2px solid transparent; margin-bottom:1px;">Slides</a>'
        '<a href="/meetings" target="_self" style="display:block; padding:7px 10px; '
        'font-family:DM Sans, sans-serif; font-size:14px; color:var(--ink-dim); '
        'text-decoration:none; border-left:2px solid transparent; margin-bottom:1px;">Meetings</a>',
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div style='position:fixed; bottom:18px; left:18px; "
        "font-family:DM Mono, monospace; font-size:10px; "
        "color:var(--ink-faint); letter-spacing:0.05em;'>"
        "STATUS &nbsp; <span style='color:var(--ink-dim)'>ONLINE</span>"
        "</div>",
        unsafe_allow_html=True,
    )

# ---- main: chat -----------------------------------------------------------
page_header(
    eyebrow="Workspace / Chat",
    title="Ask Praxis",
    subtitle="Your agent has context across todos, calendar, sheets, slides, and meetings.",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.markdown(
        """
        <div class="px-panel" style="margin-bottom:18px;">
            <div class="px-eyebrow" style="margin-bottom:8px;">Try asking</div>
            <div style="font-size:13px; color:var(--ink-dim); line-height:1.7;">
                "What's on my calendar tomorrow?"<br>
                "Summarize last week's meeting notes"<br>
                "Add a todo to review the Q3 report"
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    response = chat(prompt)

    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)