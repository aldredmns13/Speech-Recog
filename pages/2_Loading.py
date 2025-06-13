import streamlit as st
import time

st.title("⏳ Cleaning Your Audio...")

with st.spinner("Processing..."):
    time.sleep(2)  # Simulated loading
    st.switch_page("pages/3_Result.py")
