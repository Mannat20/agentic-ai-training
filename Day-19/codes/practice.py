import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <elevenlabs-convai agent-id="agent_5901ky1tvv0bfwysz9b8rkb7sw00"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>
    """,
    height=600,
)