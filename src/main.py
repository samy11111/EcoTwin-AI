"""
EcoTwin AI - Main Entry Point
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.city import City
from datahub.geocoding import Geocoder
from datahub.climate import ClimateService
from datahub.urbanism import UrbanismService # <-- Nouvel import

def main():
    print("==================================================")
    print("              Welcome to EcoTwin AI               ")
    print("==================================================")
    
    target_city_name = input("\nEnter the name of a city to analyze (e.g., Toronto): ").strip()
    if not target_city_name:
        target_city_name = "Toronto"

    my_city = City(name=target_city_name)
    
    # 1. Geocoding
    geocoder = Geocoder()
    location_data = geocoder.get_location_data(my_city.name)
    
    if location_data:
        my_city.latitude = location_data["latitude"]
        my_city.longitude = location_data["longitude"]
        my_city.country = location_data["country"]
        
        # 2. Climate & Air Quality
        climate_service = ClimateService()
        
        weather_data = climate_service.get_climate_data(my_city.latitude, my_city.longitude)
        my_city.temperature_c = weather_data.get("temperature_c")
        my_city.humidity_percent = weather_data.get("humidity_percent")
        my_city.precipitation_mm = weather_data.get("precipitation_mm")
        my_city.wind_speed_kmh = weather_data.get("wind_speed_kmh")
        
        air_data = climate_service.get_air_quality_data(my_city.latitude, my_city.longitude)
        my_city.pm2_5 = air_data.get("pm2_5")
        my_city.pm10 = air_data.get("pm10")
        my_city.aqi = air_data.get("aqi")

        # 3. Urbanism Data
        urban_service = UrbanismService()
        urban_data = urban_service.get_urban_metrics(my_city.latitude, my_city.longitude)
        my_city.road_length_km = urban_data.get("road_length_km")
        my_city.intersections_count = urban_data.get("intersections_count")

    # Affichage final
    my_city.display_summary()

if __name__ == "__main__":
    main()