import streamlit as st

st.title("🚀 Start Audio Cleaning Journey")

option = st.radio("How would you like to provide your audio?", ["🎤 Use Microphone", "📁 Upload WAV File"])

if st.button("Next ➡️"):
    if option == "🎤 Use Microphone":
        st.session_state.input_method = "mic"
    else:
        st.session_state.input_method = "file"
    st.switch_page("pages/2_Loading.py")
