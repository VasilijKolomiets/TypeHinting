from typing import Literal

from datetime import datetime

import requests

import config
from models import GeoLocation, Weather, WeatherType, Latitude, Longitude


def get_weather_response(location: GeoLocation) -> dict:
    """Get response from weather service."""
    
    # raise ValueError("ApiServiceError - no coordinates for `get_weather_response()`")
    return _get_openweather_response(location.latitude, location.longitude)


def _get_openweather_response(latitude: Latitude, longitude: Longitude) -> dict:
    # params = dict(lat=latitude, lon=longitude, appid=OWM_API_TOKEN, units="metric", lang="ua")
    # Lviv::  lat=49.8383, lon=24.0232,
    geo_coords = {
        config.weather_geo_params_names["latitude"]: latitude.value, 
        config.weather_geo_params_names["longitude"]: longitude.value,
        }
    params = config.weather_token | geo_coords | config.weather_params 

    response = requests.get(
        config.WEATHER_URL,  # "https://api.openweathermap.org/data/2.5/weather",
        params=params,
        timeout=10,
    )
    # may be raise exception here indeed ...
    return response.json() if response else {"found": False}

def parse_weather_response(openweather_dict: dict) -> Weather:
    """Parse the weather service respose JSON to  standart `Weather` type."""
    # https://openweathermap.org/current?API%20response#example_JSON

    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        description=openweather_dict["weather"][0]["description"],  # ))
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> float:  # Celsius:
    return round(openweather_dict["main"]["temp"])


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    weather_type_id = str(openweather_dict["weather"][0]["id"])

    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "8": WeatherType.CLOUDS,
    }
    
    # for _id, _weather_type in weather_types.items():
    #     if weather_type_id.startswith(_id):
    #         return _weather_type

    key = "800" if weather_type_id == "800" else weather_type_id[:1] 
    try: 
        return weather_types[key]
    except KeyError:
        raise ValueError(F"ApiServiceError {weather_type_id=}")


def _parse_sun_time(
        openweather_dict: dict, 
        time: Literal["sunrise"] | Literal["sunset"],
) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict.get("name", "Місцина без назви")  # TODO: )


if __name__ == "__main__":
    # lat=49.8383, lon=24.0232  == Lviv
    print(
        parse_weather_response(
            get_weather_response(
                GeoLocation(
                    latitude=Latitude(value=49.8383), 
                    longitude=Longitude(value=24.0232),
                )
            )
        )
    )
