commit `logger`:
 
 - added my_log.py code
    used: Protocol
    created: SimpleLogger(Protocol), LoggerInitOnly, 
    PlainFileLogger(LoggerInitOnly), SQLiteFileLogger(LoggerInitOnly),
    log_it(text: str, logger: SimpleLogger)

 - added  geolocation.py code
    created: location() -> GeoLocation

 - added weather_api_service.py
    created:
        get_weather_response(location: GeoLocation) -> dict:, 
        parse_weather_response(rew_weather: dict) -> Weather:

 - added weather_formater.py
        created:  format_weather(weather: Weather) -> str:

 - modified main.py code

 - modified models.py
    added WeatherType, Weather - classes