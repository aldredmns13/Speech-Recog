import numpy as np
import noisereduce as nr
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
import streamlit as st

def normalize_audio(audio):
    max_val = np.max(np.abs(audio))
    return audio if max_val == 0 else audio / max_val * 0.9

def reduce_noise(audio, sr):
    return nr.reduce_noise(y=audio, sr=sr)

def bandpass_filter(audio, sr=16000, lowcut=500.0, highcut=2800.0):
    nyq = 0.5 * sr
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(6, [low, high], btype='band')
    return lfilter(b, a, audio)

def amplify_audio(audio, gain=2.0):
    return np.clip(audio * gain, -1.0, 1.0)

def plot_waveform(audio, sr, title):
    fig, ax = plt.subplots()
    t = np.linspace(0, len(audio) / sr, len(audio))
    ax.plot(t, audio)
    ax.set_title(title)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    st.pyplot(fig)
