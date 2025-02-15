# Geolocation API

This is a simple FastAPI-based geolocation API that returns the nearest city and country based on latitude and longitude coordinates. The data is sourced from [GeoNames](https://www.geonames.org/), a free geographical database.

## Features
- Returns the nearest city and country based on user-provided coordinates.
- Uses the Haversine formula to calculate distances between locations.
- Filters results within a 5 km radius.
- Optimized for fast lookups with preloaded JSON data.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Run the API:
   ```sh
   poetry run fastapi dev .\app\main.py
   ```

## API Usage

### Get the nearest location
**Endpoint:**
```
GET /get-nearest-location?lat={latitude}&lon={longitude}
```

**Example Request:**
```
GET /get-nearest-location?lat=40.7128&lon=-74.0060
```

**Example Response:**
```json
{
    "nearest_city": {
        "city": "New York",
        "country": "United States",
        "distance_km": 2.5
    }
}
```

If no city is found within 5 km, it returns:
```json
{
    "nearest_city": null
}
```

## Data Source
This project uses data from **GeoNames**. The dataset includes major cities and their corresponding latitude, longitude, and country.

**GeoNames Attribution:**
- The city and country data is sourced from [GeoNames](https://www.geonames.org/).
- GeoNames data is provided under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).

## License
This project does not include a specific license. Please ensure compliance with GeoNames' attribution requirements when using this dataset.

## Contributing
Pull requests are welcome! If you'd like to improve performance or add features, feel free to contribute.

---

