from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic
import random
import folium
import os

def find_district(address):
    geocoder_api_server = f"https://geocode-maps.yandex.ru/1.x/"
    geocode_params = {
        "geocode": address,
        "format": "json",
        "kind": "district",
        "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
    }
    response = requests.get(geocoder_api_server, params=geocode_params).json()
    try:
        district = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']['SubAdministrativeArea']['SubAdministrativeAreaName']
        print(f"Район: {district}")
    except (KeyError, IndexError):
        print("Не удалось определить")

address = input("Введите адрес: ")
find_district(address)