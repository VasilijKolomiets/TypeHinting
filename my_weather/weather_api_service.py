from datetime import datetime

from models import GeoLocation, Weather, WeatherType


def get_weather_response(location: GeoLocation) -> dict:
    return dict()


def parse_weather_response(rew_weather: dict) -> Weather:
    return Weather(
        temperature=33,
        weather_type=WeatherType("Ясно"),
        sunrise=datetime.now(),
        sunset=datetime.now(),
        city="Lviv",
    )
