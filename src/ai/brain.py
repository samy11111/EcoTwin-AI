import os
from dotenv import load_dotenv
from google import genai

# Chargement de la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

class AIBrain:
    def __init__(self):
        self.client = genai.Client(api_key=api_key)

    def analyze_city(self, city):
        prompt = f"""
        You are an expert in sustainable urban planning and a data scientist. 
        Analyze the real-time data for {city.name} ({city.country}):
        - EcoScore: {city.eco_score}/100
        - Temperature: {city.temperature_c}°C
        - Air Quality (AQI): {city.aqi}
        - Infrastructure: {city.road_length_km}km of roads, {city.intersections_count} intersections.
        
        Your mission: 
        1. Provide a short, punchy diagnostic of the city's current ecological state.
        2. Propose 3 concrete, data-driven solutions to improve its EcoScore.
        
        Format your response clearly. You MUST answer entirely in English. Maintain a strict, scientific, and professional tone without fluff.
        """
        
        response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        return response.text
    