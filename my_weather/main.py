"""The aplication determine the current location weather and save it in 
    formatted structure.

"""
from pathlib import Path
import time

import geolocation as geo
from weather_api_service import get_weather_response, parse_weather_response
from weather_formatter import format_weather
from my_log import log_it, SQLiteFileLogger, PlainFileLogger

if __name__ == '__main__':
    # get my geoposition - coordinates `longitude` & `latitude`.
    location = geo.location()
    # get weather current data in JSON
    weather_raw_data = get_weather_response(location)
    # convert received data into standard JSON  <--
    weather = parse_weather_response(weather_raw_data)
    # format standartized JSON data into `text` with pattern
    text = format_weather(weather)
    # save (logging) last `text` into specified `DataBase`
    logger = PlainFileLogger(Path().cwd() / "plain.csv")  #  33
    logger = SQLiteFileLogger(Path().cwd() / 'logging.db3')
    log_it(text, logger)

    time.sleep(3)
    weather_raw_data = get_weather_response(location)
    # convert received data into standard JSON  <--
    weather = parse_weather_response(weather_raw_data)
    # format standartized JSON data into `text` with pattern
    text = format_weather(weather)
    log_it(text, logger)
    