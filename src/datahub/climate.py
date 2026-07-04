"""
EcoTwin AI - Climate and Air Quality Service
Fetches real-time weather and environmental data using Open-Meteo APIs safely.
"""

import requests
import requests_cache
import os

cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'cache')
requests_cache.install_cache(os.path.join(cache_dir, 'climate_cache'), expire_after=3600)

class ClimateService:
    """Handles weather and air quality data retrieval."""
    
    def get_climate_data(self, lat: float, lon: float) -> dict:
        """Fetches temperature, humidity, wind, and precipitation."""
        print("[*] Fetching Weather data from Open-Meteo...")
        url = "https://api.open-meteo.com/v1/forecast"
        
        # Utilisation d'un dictionnaire pour sécuriser la création de l'URL
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('current', {})
            print("[+] Success: Weather data retrieved.")
            return {
                "temperature_c": data.get("temperature_2m"),
                "humidity_percent": data.get("relative_humidity_2m"),
                "precipitation_mm": data.get("precipitation"),
                "wind_speed_kmh": data.get("wind_speed_10m")
            }
        except Exception as e:
            print(f"[-] Error fetching weather data: {e}")
            return {}

    def get_air_quality_data(self, lat: float, lon: float) -> dict:
        """Fetches PM2.5, PM10, and European AQI."""
        print("[*] Fetching Air Quality data from Open-Meteo...")
        url = "https://air-quality-api.open-meteo.com/v1/air-quality"
        
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "pm10,pm2_5,european_aqi"
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json().get('current', {})
            print("[+] Success: Air Quality data retrieved.")
            return {
                "pm2_5": data.get("pm2_5"),
                "pm10": data.get("pm10"),
                "aqi": data.get("european_aqi")
            }
        except Exception as e:
            print(f"[-] Error fetching air quality data: {e}")
            return {}