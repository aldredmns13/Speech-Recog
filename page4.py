import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import numpy as np
import soundfile as sf
import librosa
import matplotlib.pyplot as plt
from io import BytesIO
from utils.dsp import *

st.title("🎧 Your Cleaned Audio")

sr = 48000

def display_result(audio, sr):
    st.subheader("🔊 Original Audio")
    buf1 = BytesIO()
    sf.write(buf1, audio, sr, format='wav')
    st.audio(buf1)

    plot_waveform(audio, sr, "Original Audio")

    cleaned = normalize_audio(audio)
    cleaned = reduce_noise(cleaned, sr)
    cleaned = bandpass_filter(cleaned, sr)
    cleaned = amplify_audio(cleaned)
    cleaned = normalize_audio(cleaned)

    st.subheader("🧼 Cleaned Audio")
    buf2 = BytesIO()
    sf.write(buf2, cleaned, sr, format='wav')
    st.audio(buf2)
    plot_waveform(cleaned, sr, "Cleaned Audio")
    st.download_button("⬇️ Download Cleaned Audio", buf2.getvalue(), "cleaned_audio.wav", mime="audio/wav")

# Logic based on session input
input_method = st.session_state.get("input_method", None)

if input_method == "file":
    uploaded = st.file_uploader("Upload your WAV file", type=["wav"])
    if uploaded:
        y, _ = librosa.load(uploaded, sr=sr)
        display_result(y, sr)

elif input_method == "mic":
    class AudioProcessor(AudioProcessorBase):
        def __init__(self):
            self.frames = []

        def recv(self, frame):
            audio = frame.to_ndarray().flatten().astype(np.float32) / 32000.0
            self.frames.append(audio)
            return frame

    webrtc_ctx = webrtc_streamer(
        key="mic-audio",
        audio_processor_factory=AudioProcessor,
        media_stream_constraints={"audio": True, "video": False},
        async_processing=True,
    )

    if st.button("✅ Process Mic Recording"):
        if webrtc_ctx.audio_processor:
            raw = np.concatenate(webrtc_ctx.audio_processor.frames)
            audio = raw[-sr * 10:] if len(raw) > sr * 10 else raw
            display_result(audio, sr)
        else:
            st.warning("No audio recorded yet.")
else:
    st.warning("Go back to the homepage to choose an input method.")
