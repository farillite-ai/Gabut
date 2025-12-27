import streamlit as st
import time

st.set_page_config(page_title="Malu-Malu", layout="centered")

# ===== STYLE =====
st.markdown("""
<style>
.stApp {
background-color: black;
}

.center {
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
}

.text {
color: white;
font-size: 28px;
letter-spacing: 2px;
animation: pulse 2.5s infinite;
}

@keyframes pulse {
0% { opacity: 0.4; }
50% { opacity: 1; }
100% { opacity: 0.4; }
}
</style>
""", unsafe_allow_html=True)

# ===== AUDIO YOUTUBE (DISEMBUNYIKAN) =====
st.components.v1.html("""
<iframe width="0" height="0"
src="https://www.youtube.com/embedvgp0yZ8gaEs?start=60&end=80&autoplay=1"
frameborder="0"
allow="autoplay">
</iframe>
""", height=0)

# ===== TEKS DI TENGAH =====
texts = [
    "diam itu terasa",
    "mata tak berani bicara",
    "tapi hati sudah lebih dulu"
]

st.markdown("<div class='center'>", unsafe_allow_html=True)
box = st.empty()

for t in texts:
    box.markdown(f"<div class='text'>{t}</div>", unsafe_allow_html=True)
    time.sleep(6)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
