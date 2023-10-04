import requests

# Получаем данные о погоде в текущей локации пользователя
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "lat": "55.7522",  # Широта Москвы
    "lon": "37.6156",  # Долгота Москвы
    "appid": "09b69d775c5f23dfd7beac6754b6a205",  # OpenWeatherMap
    "units": "metric"  # Единицы измерения: градусы Цельсия
}
response = requests.get(url, params=params)
data = response.json()

# Анализируем данные о погоде
if data.get("main"):
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
else:
    temperature = "неизвестно"
    humidity = "неизвестно"

if data.get("wind"):
    wind_speed = data["wind"]["speed"]
else:
    wind_speed = "неизвестно"

# Определяем тип погоды с наибольшей вероятностью
if temperature == "неизвестно":
    print("Не удалось получить данные о температуре")
elif temperature < 10:
    print("Скорее всего, вы находитесь внутри помещения (холодно)")
elif humidity > 70:
    print("Скорее всего, вы находитесь внутри помещения (высокая влажность)")
elif wind_speed == "неизвестно":
    print("Не удалось получить данные о скорости ветра")
elif wind_speed > 5:
    print("Скорее всего, вы находитесь на улице (ветрено)")
else:
    print("Скорее всего, вы находитесь на улице (хорошая погода)")

print("Температура: ", temperature)
print("Влажность: ", humidity)
print("Скорость ветра: ", wind_speed)