from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic

geocoder_api_server = "4d5cf577-a59e-4cd7-a012-4ca4c9f98429"
search_api_server = "b704cfa1-597c-4673-bb90-a9559f5c7d91"


def find_nearest_pharmacy(address: str):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": address,
        "format": "json",
        "apikey": geocoder_api_server
    }

    try:
        response = requests.get(geocode_url, params=geocode_params)
        response.raise_for_status()
        location_data = response.json()

        point = location_data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = tuple(map(float, point.split()))
        print(f"Координаты адреса: {coords}")

    except (KeyError, IndexError):
        print("Не удалось найти координаты для данного адреса.")
        return
    except requests.RequestException as e:
        print(f"Ошибка при запросе геокодирования: {e}")
        return

    search_url = "https://search-maps.yandex.ru/v1/"
    search_params = {
        "apikey": search_api_server,
        "text": "аптека",
        "ll": f"{coords[0]},{coords[1]}",
        "type": "biz",
        "lang": "ru_RU",
        "results": 5,
    }

    try:
        search_response = requests.get(search_url, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()

        if 'features' in search_data and search_data['features']:
            pharmacy = search_data['features'][0]
            pharmacy_name = pharmacy['properties']['CompanyMetaData']['name']
            pharmacy_address = pharmacy['properties']['CompanyMetaData'].get('address', 'Адрес не указан')
            print(f"Ближайшая аптека: {pharmacy_name}, адрес: {pharmacy_address}")
        else:
            print("Аптеки поблизости не найдены.")

    except requests.RequestException as e:
        print(f"Ошибка при запросе поиска аптек: {e}")


if __name__ == "__main__":
    user_address = input("Введите адрес: ")
    find_nearest_pharmacy(user_address)