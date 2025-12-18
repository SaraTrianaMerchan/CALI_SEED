# === weather_api.py ===
# Integration with OpenWeatherMap API for real-time weather data
# Get your free API key at: https://openweathermap.org/api

import os
import requests
from datetime import datetime

# OpenWeatherMap API configuration
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Locations coordinates (Aragon, Spain)
LOCATIONS = {
    'Zaragoza': {'lat': 41.6488, 'lon': -0.8891},
    'Huesca': {'lat': 42.1401, 'lon': -0.4080},
    'Teruel': {'lat': 40.3456, 'lon': -1.1065}
}

def get_weather_data(location='Zaragoza'):
    """
    Fetch real-time weather data from OpenWeatherMap

    Args:
        location (str): City name (Zaragoza, Huesca, or Teruel)

    Returns:
        dict: Weather data or None if error
    """
    if not WEATHER_API_KEY:
        return {
            'error': 'OPENWEATHER_API_KEY not configured',
            'message': 'Please add your OpenWeatherMap API key to environment variables'
        }

    if location not in LOCATIONS:
        return {'error': f'Location {location} not supported'}

    coords = LOCATIONS[location]

    try:
        params = {
            'lat': coords['lat'],
            'lon': coords['lon'],
            'appid': WEATHER_API_KEY,
            'units': 'metric',  # Celsius
            'lang': 'es'        # Spanish
        }

        response = requests.get(WEATHER_API_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        # Transform to our format
        weather_info = {
            'location': location,
            'timestamp': datetime.utcnow().isoformat(),
            'temperature_c': round(data['main']['temp'], 1),
            'feels_like_c': round(data['main']['feels_like'], 1),
            'humidity_percent': data['main']['humidity'],
            'pressure_hpa': data['main']['pressure'],
            'wind_speed_kmh': round(data['wind']['speed'] * 3.6, 1),  # m/s to km/h
            'wind_direction': data['wind'].get('deg', 0),
            'clouds_percent': data['clouds']['all'],
            'visibility_km': data.get('visibility', 10000) / 1000,
            'weather_main': data['weather'][0]['main'],
            'weather_description': data['weather'][0]['description'],
            'weather_icon': data['weather'][0]['icon'],
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).isoformat(),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).isoformat(),
            'rainfall_mm': data.get('rain', {}).get('1h', 0),  # Last 1 hour
            'source': 'OpenWeatherMap',
            'is_real_time': True
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        return {
            'error': 'API request failed',
            'message': str(e)
        }
    except Exception as e:
        return {
            'error': 'Unexpected error',
            'message': str(e)
        }

def get_all_locations_weather():
    """
    Get weather data for all Aragon locations

    Returns:
        list: Weather data for all locations
    """
    results = []
    for location in LOCATIONS.keys():
        weather = get_weather_data(location)
        if weather and 'error' not in weather:
            results.append(weather)
    return results

def check_weather_alerts(weather_data):
    """
    Check if weather data triggers any alerts

    Args:
        weather_data (dict): Weather data

    Returns:
        list: List of alerts detected
    """
    alerts = []

    # Temperature alerts
    if weather_data.get('temperature_c', 0) > 35:
        alerts.append('Temperatura alta - Riesgo de ola de calor')
    if weather_data.get('temperature_c', 0) < 0:
        alerts.append('Temperatura bajo cero - Riesgo de heladas')

    # Humidity alerts
    if weather_data.get('humidity_percent', 50) < 20:
        alerts.append('Humedad muy baja - Riesgo de incendios')

    # Wind alerts
    if weather_data.get('wind_speed_kmh', 0) > 70:
        alerts.append('Vientos fuertes - Posible tormenta')

    # Rain alerts
    if weather_data.get('rainfall_mm', 0) > 20:
        alerts.append('Lluvia intensa - Riesgo de inundación')

    return alerts

if __name__ == '__main__':
    # Test the API
    print("\n🌤️ Testing OpenWeatherMap Integration\n")

    for location in LOCATIONS.keys():
        print(f"\n📍 {location}:")
        weather = get_weather_data(location)

        if 'error' in weather:
            print(f"  ❌ Error: {weather.get('message')}")
        else:
            print(f"  🌡️ Temperature: {weather['temperature_c']}°C")
            print(f"  💧 Humidity: {weather['humidity_percent']}%")
            print(f"  💨 Wind: {weather['wind_speed_kmh']} km/h")
            print(f"  ☁️ Description: {weather['weather_description']}")

            alerts = check_weather_alerts(weather)
            if alerts:
                print(f"  ⚠️ Alerts: {', '.join(alerts)}")
