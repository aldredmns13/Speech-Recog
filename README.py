# 🎤 Speech Preprocessing App

This is a multipage Streamlit web app for cleaning and analyzing speech audio. It allows users to:

- Record audio through a microphone
- Upload WAV audio files
- Apply digital signal processing:
  - Normalization
  - Noise reduction
  - Bandpass filtering
  - Amplification
- Compare original and cleaned audio
- Download the cleaned version

## 📁 Folder Structure

```
speech-cleaner/
├── Home.py                     # Homepage with button to start journey
├── pages/
│   ├── 1_NewJourney.py         # Audio input choice (mic or file)
│   ├── 2_Loading.py            # Loading screen (optional visual cue)
│   ├── 3_Result.py             # Cleaned audio + MATLAB-like plots
├── utils/
│   └── dsp.py                  # Audio cleaning logic
├── assets/
│   └── wave_icon.png           # Optional image used in homepage
├── requirements.txt
└── README.md

```

## 🚀 How to Run

1. Clone or download the repo:
```bash
git clone https://github.com/YOUR_USERNAME/speech_preprocessing_app.git
cd speech_preprocessing_app
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt

pip install streamlit streamlit-webrtc numpy soundfile librosa matplotlib noisereduce scipy
```

4. Run the app:
```bash
streamlit run Home.py
mv pages/Home.py .

```

## 🛠 Requirements

- Python 3.8+
- Streamlit
- streamlit-webrtc
- NumPy, Librosa, Matplotlib
- noisereduce, scipy, av

