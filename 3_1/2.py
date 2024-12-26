from PIL import Image
import requests
from io import BytesIO
from geopy.distance import geodesic

api_key = "9e0719e2-75a8-4ef4-bd2e-097eb7ff72d8"

address_ll = "37.440262,55.818015"
delta = "0.3"

points_location = {"1": "37.554191,55.715551",
                     "2": "37.440262,55.818015",
                     "3": "37.559809,55.791540"
                     }

coordinate_strings = list(points_location.values())
pl = ",".join(coordinate_strings)


map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pl": pl,
    "z": "10",
    "pt": "37.440262,55.818015",
    "size": "300,300"
}

coordinates = []
for point in points_location.values():
    lat, lon = map(float, point.split(','))
    coordinates.append((lat, lon))

total_distance = 0
for i in range(len(coordinates) - 1):
    total_distance += geodesic(coordinates[i], coordinates[i+1]).km

print(f"Общая длина пути (geopy): {total_distance:.2f} км")

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()