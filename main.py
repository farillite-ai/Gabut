import streamlit as st
import time

st.set_page_config(page_title="Malu-Malu", layout="centered")

# ===== STYLE: HITAM + EFEK HALUS =====
st.markdown("""
<style>
.stApp {
background-color: #000000;
}

.container {
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 80vh;
}

.text {
color: #ffffff;
font-size: 26px;
letter-spacing: 2px;
animation: pulse 2s infinite;
}

@keyframes pulse {
0% { opacity: 0.4; }
50% { opacity: 1; }
100% { opacity: 0.4; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='container'>", unsafe_allow_html=True)

# ===== YOUTUBE EMBED (1:00 - 1:20) =====
st.components.v1.html("""
<iframe width="300" height="170"
src="https://www.youtube.com/embed/vgp0yZ8gaEs?start=60&end=80&controls=0"
frameborder="0"
allow="autoplay">
</iframe>
""", height=180)

# ===== TEKS (SINGKAT, TENANG) =====
texts = [
    "diam itu berbunyi",
    "mata tak berani jujur",
    "tapi hati sudah duluan"
]

box = st.empty()

for t in texts:
    box.markdown(f"<div class='text'>{t}</div>", unsafe_allow_html=True)
    time.sleep(6)

st.markdown("</div>", unsafe_allow_html=True)
