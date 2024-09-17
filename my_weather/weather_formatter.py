from models import Weather
import config

fmt = config.weather_fmt

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return fmt.format(
        city=weather.city,
        temperature=weather.temperature,
        weather_type=weather.weather_type.value,
        sunrise=weather.sunrise,
        sunset=weather.sunset,
    )


if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType

    weather = Weather(
        temperature=28.0,
        weather_type=WeatherType.CLOUDS,
        description="руки не бачу",
        sunrise=datetime.fromisoformat("2022-05-03 04:00:00"),
        sunset=datetime.fromisoformat("2022-05-03 20:25:00"),
        city="Львів",
    )
    print(format_weather(weather))
