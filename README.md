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
speech_preprocessing_app/
├── Home.py                  # Homepage UI
├── pages/
│   └── NewJourney.py        # Audio cleaning workflow
├── requirements.txt         # Required Python packages
└── README.md                # Project overview
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
```

4. Run the app:
```bash
streamlit run Home.py
```

## 🛠 Requirements

- Python 3.8+
- Streamlit
- streamlit-webrtc
- NumPy, Librosa, Matplotlib
- noisereduce, scipy, av

