import configparser

# Створення об'єкта парсера
config = configparser.ConfigParser()
config_token = configparser.ConfigParser()

# Читання файлу налаштувань
config.read("config.ini")

# Зчитування назви файлу до токенів сервісу погоди
token_ini_file = config["TOKEN_FILES"]["weather_file"]
print(token_ini_file)
# Отримання секції 'weather_params' і перетворення її в словник для майбутнього `params`
weather_params = dict(config["weather_params"])
print(weather_params)

weather_geo_params_names = dict(config["weather_geo_params_names"])
print(weather_geo_params_names)

WEATHER_URL = config["weather_url"]["weather_url"]


# Читання файлу налаштувань з токеном
config_token.read(token_ini_file)
weather_token = dict(config_token["openweather"])
print(weather_token)