# 🌍 EcoTwin AI : Real-Time Urban Digital Twin

EcoTwin AI is a Python-based Digital Twin engine that analyzes the real-time ecological and infrastructural health of any city in the world. 

It aggregates live data (Weather, Air Quality, Urban density) and uses the Google Gemini AI to generate expert sustainability reports.

## 🚀 Features
* **Live API Integrations:** Fetches real-time data from Nominatim, Open-Meteo, and OpenStreetMap.
* **Resilient Architecture:** Implements a graceful degradation Fail-Safe if external OSM servers timeout.
* **Scientific EcoScore:** Calculates a strict 0-100 score based on WHO guidelines and LEED urban standards.
* **AI Brain:** Uses Google GenAI (`gemini-2.5-flash`) to generate actionable, data-driven urban planning solutions.

## ⚙️ Installation
1. Clone the repository:
   `git clone https://github.com/TON_NOM_UTILISATEUR/EcoTwin-AI.git`
2. Create a virtual environment:
   `python -m venv venv`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Set up your `.env` file with your Google Gemini API key:
   `GEMINI_API_KEY=your_api_key_here`

## 🏃‍♂️ Usage
Run the main pipeline:
`python src/main.py`