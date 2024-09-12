Программа показывает погоду по текущим GPS координатам. Координаты берутся
из программы `whereami`, которая работает (и работает отлично!) на компьютерах
Mac. [О whereami](https://github.com/robmathers/WhereAmI).

Получение погоды по координатам происходит в сервисе
[OpenWeather](https://openweathermap.org/api).

Для запуска используйте python 3.10 (внешние библиотеки не требуются для работы
приложения), в `config.py` проставьте API ключ для доступа к OpenWeather и 
запустите:


```bash
./weather
```

Файл `weather` — исполнимый файл с python кодом, его можно открыть посмотреть.

Данный материал подготовлен в качестве примера к [видео](https://www.youtube.com/watch?v=dKxiHlZvULQ) и [книге
«Типизированный Python»](https://t.me/t0digital/151).


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


