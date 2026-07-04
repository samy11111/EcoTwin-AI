"""
EcoTwin AI - City Model
This module defines the core City class, representing our Digital Twin.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class City:
    """
    Represents a digital twin of a city, holding all its sustainability data.
    Using @dataclass automatically generates the initialization methods.
    """
    # Identity
    name: str
    country: Optional[str] = None

    # Geography
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    area_sq_km: Optional[float] = None

    # Demography
    population: Optional[int] = None
    density: Optional[float] = None

    # Climate
    temperature_c: Optional[float] = None
    humidity_percent: Optional[float] = None
    wind_speed_kmh: Optional[float] = None
    precipitation_mm: Optional[float] = None

    # Air Quality
    pm2_5: Optional[float] = None
    pm10: Optional[float] = None
    aqi: Optional[int] = None

    # Urban Planning
    buildings_count: Optional[int] = None
    road_length_km: Optional[float] = None
    intersections_count: Optional[int] = None
    green_spaces_sq_km: Optional[float] = None
    forests_sq_km: Optional[float] = None
    lakes_sq_km: Optional[float] = None
    rivers_sq_km: Optional[float] = None
    bike_paths_km: Optional[float] = None
    public_transport_routes: Optional[int] = None

    # EcoScore & EcoDNA
    eco_score: Optional[float] = None
    eco_dna: Optional[str] = None

    def display_summary(self) -> None:
        """Prints a formatted summary of the city's current data."""
        print(f"\n==========================================")
        print(f"        DIGITAL TWIN: {self.name.upper()}         ")
        print(f"==========================================")
        
        print("\n🌍 [IDENTITY & GEOGRAPHY]")
        print(f"  - Country:   {self.country or 'N/A'}")
        print(f"  - Latitude:  {self.latitude or 'N/A'}")
        print(f"  - Longitude: {self.longitude or 'N/A'}")
        
        print("\n🌤️  [CLIMATE]")
        print(f"  - Temperature:   {self.temperature_c} °C" if self.temperature_c is not None else "  - Temperature:   N/A")
        print(f"  - Humidity:      {self.humidity_percent} %" if self.humidity_percent is not None else "  - Humidity:      N/A")
        print(f"  - Wind Speed:    {self.wind_speed_kmh} km/h" if self.wind_speed_kmh is not None else "  - Wind Speed:    N/A")
        print(f"  - Precipitation: {self.precipitation_mm} mm" if self.precipitation_mm is not None else "  - Precipitation: N/A")

        print("\n💨 [AIR QUALITY]")
        print(f"  - PM2.5: {self.pm2_5} µg/m³" if self.pm2_5 is not None else "  - PM2.5: N/A")
        print(f"  - PM10:  {self.pm10} µg/m³" if self.pm10 is not None else "  - PM10:  N/A")
        print(f"  - AQI:   {self.aqi} (European Index)" if self.aqi is not None else "  - AQI:   N/A")

        print("\n🏙️  [URBANISM (Core 3km radius)]")
        print(f"  - Road Length:   {self.road_length_km} km" if self.road_length_km is not None else "  - Road Length:   N/A")
        print(f"  - Intersections: {self.intersections_count}" if self.intersections_count is not None else "  - Intersections: N/A")
        
        print("\n==========================================\n")