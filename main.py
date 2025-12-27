import streamlit as st
import time

st.set_page_config(page_title="Malu-Malu", layout="wide")

# ===== BACKGROUND =====
st.markdown("""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1500530855697-b586d89ba3ee");
background-size: cover;
background-position: center;
}
.lyrics {
font-size: 30px;
color: white;
text-align: center;
text-shadow: 2px 2px 10px black;
animation: fade 2s;
}
@keyframes fade {
from {opacity: 0;}
to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

st.title("🎵 Malu-Malu")

# ===== AUDIO (ONLINE LINK) =====
audio_url = "ISI_LINK_MP3_DI_SINI"
st.audio(audio_url, start_time=60)

# ===== LIRIK (ISI SENDIRI) =====
lyrics = [
    "🎶 Baris 1 (lu isi sendiri)",
    "🎵 Baris 2",
    "💭 Baris 3",
    "❤️ Baris 4"
]

box = st.empty()

for line in lyrics:
    box.markdown(f"<div class='lyrics'>{line}</div>", unsafe_allow_html=True)
    time.sleep(5)
