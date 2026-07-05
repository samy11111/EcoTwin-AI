"""
EcoTwin AI - Scoring & EcoDNA Engine
Calculates a STRICT scientific EcoScore based on WHO and LEED urban standards.
"""

class EcoAnalyzer:
    """Engine to analyze urban metrics and generate sustainability scores."""

    def calculate_eco_score(self, city) -> float:
        """
        Calculates a highly strict score from 0 to 100. 
        Leaves room for AI optimization.
        """
        if city.aqi is None or city.temperature_c is None or city.road_length_km is None:
            return None

        # Base score. No city is a perfect 100 due to inherent urban carbon footprint.
        score = 95.0 
        
        # 1. AIR QUALITY (WHO Strict Guidelines)
        # WHO states PM2.5 should not exceed 5 µg/m³.
        if city.pm2_5 is not None and city.pm2_5 > 5.0:
            pm_penalty = min(20.0, (city.pm2_5 - 5.0) * 1.5)
            score -= pm_penalty
            
        # Overall AQI penalty (European standard, everything > 20 is non-optimal)
        if city.aqi > 20:
            aqi_penalty = min(15.0, (city.aqi - 20) * 0.3)
            score -= aqi_penalty
                
        # 2. CLIMATE ENERGY DEMAND (Cooling / Heating)
        # Optimal human comfort with minimal HVAC energy is ~15°C to 25°C.
        if city.temperature_c > 25:
            # Cooling penalty
            score -= min(15.0, (city.temperature_c - 25) * 1.2)
        elif city.temperature_c < 10:
            # Heating penalty (often fossil fuels)
            score -= min(10.0, (10 - city.temperature_c) * 0.8)
                
        # 3. URBAN WALKABILITY vs CONCRETE FOOTPRINT
        if city.road_length_km > 0:
            # Density of intersections (Walkability)
            density = city.intersections_count / city.road_length_km
            if density < 8:
                score -= min(15.0, (8 - density) * 2)  # Low walkability penalty
                
            # Excessive concrete infrastructure (Car dependency)
            # In an 800m radius, having >15km of road means extreme concrete density.
            if city.road_length_km > 15:
                score -= min(15.0, (city.road_length_km - 15) * 0.5)

        return max(0.0, min(100.0, round(score, 1)))

    def determine_eco_dna(self, city) -> tuple:
        """
        Classifies the city (EcoDNA) using strict thresholds.
        """
        if city.eco_score is None:
            return "Unknown", "Not enough data to calculate EcoDNA."

        if city.eco_score >= 85:
            dna = "Regenerative Oasis"
            reason = "World-class environmental metrics with optimal urban flow."
        elif city.eco_score >= 70:
            dna = "Transitioning Smart City"
            reason = "Good infrastructure, but suffers from manageable pollution or concrete footprint."
        elif city.eco_score >= 50:
            dna = "Stressed Urban Environment"
            reason = "High energy demand, noticeable air pollution, and car-centric design."
        elif city.eco_score >= 35:
            dna = "High-Carbon Sprawl"
            reason = "Severe concrete heat islands and poor air quality metrics."
        else:
            dna = "Critical Industrial Zone"
            reason = "Toxic air quality and completely unsustainable urban infrastructure."

        return dna, reason