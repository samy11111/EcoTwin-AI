"""
EcoTwin AI - Urbanism Service
Fetches urban infrastructure data (roads, networks) using OpenStreetMap via OSMnx.
"""

import os
import osmnx as ox
import warnings

# Suppress visual warnings from pandas/osmnx to keep our terminal clean
warnings.filterwarnings("ignore")

# Configure OSMnx to use our cache directory
cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'cache')
ox.settings.cache_folder = os.path.join(cache_dir, 'osmnx_cache')
ox.settings.use_cache = True
ox.settings.log_console = False

class UrbanismService:
    """Handles urban infrastructure data retrieval."""

    def get_urban_metrics(self, lat: float, lon: float, radius: int = 3000) -> dict:
        """
        Fetches road network stats within a radius (default 3km) to represent the city core.
        """
        print(f"[*] Fetching Urban metrics from OpenStreetMap (Core radius: {radius}m)...")
        print("    (This might take 10 to 60 seconds the first time, please wait...)")
        
        try:
            # Download the street network for driving within the radius
            G = ox.graph_from_point((lat, lon), dist=radius, network_type='drive')
            
            # Calculate basic statistics
            stats = ox.basic_stats(G)
            
            # The street length is in meters, we convert it to km
            road_length_m = stats.get('street_length_total', 0)
            intersections = stats.get('intersection_count', 0)
            
            print("[+] Success: Urban metrics retrieved.")
            return {
                "road_length_km": round(road_length_m / 1000, 2),
                "intersections_count": intersections
            }
        except Exception as e:
            print(f"[-] Error fetching urban data: {e}")
            return {}