import streamlit as st

from api import chat


st.set_page_config(
    page_title="AI Productivity Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Productivity Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(message)

prompt = st.chat_input("Ask me anything...")

if prompt:

    st.session_state.messages.append(
        ("user", prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = chat(prompt)

    st.session_state.messages.append(
        ("assistant", response)
    )

    with st.chat_message("assistant"):
        st.markdown(response)