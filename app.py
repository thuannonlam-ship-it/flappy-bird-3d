
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Flappy Bird 3D",
    page_icon="🐤",
    layout="wide"
)

st.title("🐤 Flappy Bird 3D")

game_file = Path(__file__).parent / "game.html"

if game_file.exists():
    components.html(
        game_file.read_text(encoding="utf-8"),
        height=700,
        scrolling=False
    )
else:
    st.error("Chưa tìm thấy file game.html")
