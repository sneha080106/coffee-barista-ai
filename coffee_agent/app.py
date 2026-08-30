import asyncio
import streamlit as st
from google.adk.runners import InMemoryRunner
from google.genai import types
from agent import root_agent

st.set_page_config(
    page_title="Coffee Barista AI",
    page_icon="☕",
    layout="centered",
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at top left, rgba(196, 137, 91, 0.18), transparent 30%),
        radial-gradient(circle at bottom right, rgba(120, 72, 45, 0.20), transparent 30%),
        #120d0a;
}

/* Main content */
.block-container {
    max-width: 850px;
    padding-top: 2.5rem;
    padding-bottom: 7rem;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hero section */
.hero {
    text-align: center;
    padding: 2.2rem 1.5rem 1.8rem;
    margin-bottom: 2rem;
    border-radius: 24px;
    background: linear-gradient(
        135deg,
        rgba(80, 48, 30, 0.85),
        rgba(35, 22, 16, 0.9)
    );
    border: 1px solid rgba(212, 163, 115, 0.25);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.25);
}

.hero-icon {
    font-size: 3.5rem;
    margin-bottom: 0.4rem;
}

.hero h1 {
    color: #f5dfc5;
    font-size: 2.4rem;
    margin-bottom: 0.4rem;
}

.hero p {
    color: #c9b4a0;
    font-size: 1.05rem;
    margin: 0;
}

/* User messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: rgba(101, 61, 40, 0.55);
    border: 1px solid rgba(218, 169, 120, 0.18);
    border-radius: 18px;
    padding: 0.6rem;
    margin-bottom: 0.8rem;
}

/* Assistant messages */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 0.6rem;
    margin-bottom: 0.8rem;
}

/* Chat input */
[data-testid="stChatInput"] {
    border-radius: 18px;
}

[data-testid="stChatInput"] textarea {
    background: #241914 !important;
    color: #f5dfc5 !important;
    border-radius: 18px !important;
}

/* Small badge */
.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 30px;
    background: rgba(196, 137, 91, 0.15);
    border: 1px solid rgba(196, 137, 91, 0.3);
    color: #dcae7f;
    font-size: 0.85rem;
    margin-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="badge">✦ AI-Powered Coffee Recommendations</div>
    <div class="hero-icon">☕</div>
    <h1>Coffee Barista AI</h1>
    <p>Your personal AI barista for the perfect coffee recommendation.</p>
</div>
""", unsafe_allow_html=True)


# ---------- SESSION ----------
if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------- DISPLAY OLD MESSAGES ----------
for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "☕"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# ---------- AI AGENT ----------
async def ask_agent(prompt):

    runner = InMemoryRunner(agent=root_agent)
    user_id = "customer"

    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id=user_id,
    )

    content = types.Content(
        role="user",
        parts=[types.Part(text=prompt)]
    )

    response = ""

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session.id,
        new_message=content,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response += part.text

    return response


# ---------- CHAT ----------
if prompt := st.chat_input("Ask your AI barista anything... ☕"):

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="☕"):

        with st.spinner("Your barista is thinking..."):
            response = asyncio.run(ask_agent(prompt))

        st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
