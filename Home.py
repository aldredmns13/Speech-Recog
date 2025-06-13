import streamlit as st

st.set_page_config(page_title="Speech Recognition Preprocessing", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎤 Speech Recognition Preprocessing</h1>
    <h3 style='text-align: center;'>Clean your noisy audio with us</h3>
""", unsafe_allow_html=True)

st.image("https://img.icons8.com/clouds/500/audio-wave--v1.png", width=250)

st.markdown("### ➡️ Choose an Option Below")

if st.button("🎙 Start Audio Cleaning Journey"):
    st.switch_page("pages/1_NewJourney.py")
