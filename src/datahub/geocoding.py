"""
EcoTwin AI - Geocoding Service
Fetches geographical coordinates and country for a given city name using Nominatim API.
"""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import requests_cache
import os

cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'cache')
os.makedirs(cache_dir, exist_ok=True)

# NOUVEAU : On utilise 'geocoding_cache_v2' pour ignorer l'ancien cache
requests_cache.install_cache(os.path.join(cache_dir, 'geocoding_cache_v2'), expire_after=2592000)

class Geocoder:
    """Handles geographical data retrieval."""

    def __init__(self):
        self.geolocator = Nominatim(user_agent="ecotwin_ai_research_project")

    def get_location_data(self, city_name: str) -> dict:
        print(f"[*] Geocoding '{city_name}' via Nominatim API...")
        try:
            # NOUVEAU : Ajout de timeout=10 pour éviter les erreurs de connexion
            location = self.geolocator.geocode(
                city_name, 
                exactly_one=True, 
                addressdetails=True,
                language='en',
                timeout=10
            )

            if location:
                address = location.raw.get('address', {})
                country = address.get('country', 'Unknown')
                print(f"[+] Success: Found {city_name}, {country}")
                return {
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                    "country": country
                }
            else:
                print(f"[-] Error: Could not find location data for '{city_name}'.")
                return None

        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"[-] API Error during geocoding: {e}")
            return None