from models import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (
        f"{weather.city}, температура {weather.temperature}°C, "
        f"{weather.weather_type.value}\n"
        f"Схід: {weather.sunrise.strftime('%H:%M')}\n"
        f"Захід: {weather.sunset.strftime('%H:%M')}\n"
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
