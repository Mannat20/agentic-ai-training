import streamlit as st
import streamlit.components.v1 as components
from elevenlabs.client import ElevenLabs

st.set_page_config(page_title="French Tutor", page_icon="🇫🇷")
st.title("🇫🇷 Amélie — Your French Tutor")

elevenlabs = ElevenLabs(api_key=st.secrets["917cab1ae6fde892b0e1a440331ce1ca8e719c62b2051af3cfa5c33bb704c24b"])

AGENT_ID = "agent_5901ky1tvv0bfwysz9b8rkb7sw00"

# Get a signed URL for this session (server-side, API key used here only)
signed_url_response = elevenlabs.conversational_ai.conversations.get_signed_url(
    agent_id=AGENT_ID
)
signed_url = signed_url_response.signed_url

components.html(
    f"""
    <elevenlabs-convai signed-url="{signed_url}"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
    """,
    height=600,
)