from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic

def find_southernmost_city_yandex(city_list, api_key):
    geocoder_api_server = "https://geocode-maps.yandex.ru/1.x/"
    cities_coords = {}

    for city in city_list:
        try:
            params = {
                "apikey": api_key,
                "geocode": city.strip(),
                "format": "json"
            }
            response = requests.get(geocoder_api_server, params=params)
            if response.status_code == 200:
                geo_data = response.json()
                try:
                    pos = geo_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
                    lon, lat = map(float, pos.split())
                    cities_coords[city.strip()] = lat
                except (IndexError, KeyError):
                    print(f"Не удалось найти координаты города: {city}")
            else:
                print(f"Ошибка при запросе геокодера для города {city}: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при обработке города {city}: {e}")

    if cities_coords:
        southernmost_city = min(cities_coords, key=cities_coords.get)
        return southernmost_city
    else:
        print("Не удалось обработать ни один из городов.")
        return None



if __name__ == "__main__":
    api_key = "4d5cf577-a59e-4cd7-a012-4ca4c9f98429"
    cities = input("Введите список городов через запятую: ").split(",")
    southernmost_city = find_southernmost_city_yandex(cities, api_key)

    if southernmost_city:
        print(f"Самый южный город: {southernmost_city}")
    else:
        print("Не удалось определить самый южный город.")