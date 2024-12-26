from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic

api_key = "9e0719e2-75a8-4ef4-bd2e-097eb7ff72d8"

latitude = float(input(f"Введите широту для точки: "))
longitude = float(input(f"Введите долготу для точки: "))
address_ll = f"{latitude},{longitude}"
delta = "0.3"

map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()