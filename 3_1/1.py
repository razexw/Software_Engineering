from PIL import Image
import requests
from io import BytesIO

# search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "9e0719e2-75a8-4ef4-bd2e-097eb7ff72d8"

address_ll = "37.620070,55.753630"
delta = "1.0"
stadiums_location = {"Лужники": "37.554191,55.715551",
                     "Спартак": "37.440262,55.818015",
                     "Динамо": "37.559809,55.791540"
                     }

def addmark(stadiums):
    results = []
    for stadium, coords in stadiums.items():
        results.append(coords)
    return results

marks = addmark(stadiums_location)

map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pt": "~".join(marks),
    "size": "200,200"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()