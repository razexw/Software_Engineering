from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic
import random
import folium
import os

geocoder_api_key = "4d5cf577-a59e-4cd7-a012-4ca4c9f98429"  
cities = [
    "Москва",
    "Санкт-Петербург",
    "Казань",
    "Сочи",
    "Екатеринбург",
    "Новосибирск",
    "Владивосток",
    "Краснодар",
    "Уфа",
    "Стерлитамак",
    "Ишимбай",
    "Нефтекамск"
]


def fetch_city_coordinates(city_name):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": city_name,
        "format": "json",
        "apikey": geocoder_api_key
    }

    try:
        response = requests.get(geocode_url, params=geocode_params)
        response.raise_for_status() 
        data = response.json()
        point = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coordinates = tuple(map(float, point.split()))
        return coordinates
    except (KeyError, IndexError):
        print(f"Ошибка: Не удалось получить координаты для города '{city_name}'. Пропускаю...")
        return None
    except requests.RequestException as e:
        print(f"Ошибка при запросе геокодера: {e}. Пропускаю...")
        return None


def generate_city_map(coordinates, city_name):
    city_map = folium.Map(location=[coordinates[1], coordinates[0]], zoom_start=12,
                          tiles='cartodbpositron')  
    folium.Marker(location=[coordinates[1], coordinates[0]], icon=folium.Icon(color='red')).add_to(city_map)

    temp_filename = f"{city_name}_map.html"
    city_map.save(temp_filename)

    import webbrowser
    webbrowser.open(os.path.abspath(temp_filename))

    return temp_filename 


def play_guess_the_city():

    random.shuffle(cities)  

    for city in cities:
        print("\n*************************************************")
        print(f"Карта следующего города показывается. Попробуйте угадать!")

        coordinates = fetch_city_coordinates(city)
        if not coordinates:
            continue

        temp_filename = generate_city_map(coordinates, city)

        input("Нажмите Enter, чтобы ввести ваш ответ...")

        user_guess = input("Ваш ответ: ").strip()
        if user_guess.lower() == city.lower():
            print("Отлично! Вы угадали!")
        else:
            print(f"Неверно! Это был город '{city}'.")

        os.remove(temp_filename)

    print("\nИгра окончена. Спасибо за участие!")


if __name__ == "__main__":
    play_guess_the_city()