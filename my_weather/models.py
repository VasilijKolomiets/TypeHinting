"""The projects model`s module."""
from enum import Enum
from dataclasses import dataclass

from datetime import datetime

from pydantic import BaseModel, Field

class Latitude(BaseModel):
    """Latitude is GeoCoordinate.
    Field(..., ge=-90, le=90)
    """
    value: float = Field(..., ge=-90, le=90)

class Longitude(BaseModel):
    """Longitude is GeoCoordinate.
    Field(..., ge=-180, le=180)
    """
    value: float = Field(..., ge=-180, le=180)

class GeoLocation(BaseModel):
    """GeoLocation is the GeoCoordinates pair.
    
        latitude: Latitude
        longitude: Longitude
    """
    latitude: Latitude
    longitude: Longitude


class WeatherType(str, Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Мряка"
    RAIN = "Дощ"
    SNOW = "Сніг"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Хмарно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: float
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

    def __post_init__(self):
        if 2000 < self.temperature < -273.15:
            raise ValueError(f"{self.temperature=} is not valid")


if __name__ == '__main__':
    coords = GeoLocation(
        latitude=Latitude(value=49.8397),
        longitude=Longitude(value=24.0297)
    )
    print(coords)

    # Приклад використання
    text_value = "Туман"
    weather_type = WeatherType(text_value)
    print(weather_type)  # Output: WeatherType.FOG

    coords = GeoLocation(
        latitude=Latitude(value=-300),
        longitude=Longitude(value=200)
    )
    print(coords)
