from fastapi import FastAPI
from math import radians, sin, cos, sqrt, atan2
import json
from pydantic import Field


app = FastAPI()

# ====================================================================================== 

# Load cities data into memory once
def load_cities_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Load city data
cities_data = load_cities_json("location-info_with_population_over_500.json")

# Haversine formula for distance calculation
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c  # Distance in kilometers


@app.get("/get-nearest-location")
async def get_nearest_location(lat: float, lon: float, max_radius: int = 5):
    print(f"Received lat: {lat}, lon: {lon}")  # Debugging

    nearest_city = None
    min_distance = float('inf')

    for city in cities_data:
        distance = haversine(lat, lon, city["lat"], city["lon"])

        if distance < min_distance:
            min_distance = distance
            nearest_city = {
                "city": city["name"],
                "country": city["country"],
                "distance_km": round(distance, 2)
            }

    print(f"Nearest city found: {nearest_city}")  # Debugging

    if min_distance > max_radius:
        print("No city found within 5 km.")
        return {"nearest_city": None}

    return {"nearest_city": nearest_city}
# ====================================================================================== 
