import urllib.request
import json
import random


def weather():
    cities = ["miami", "toronto", "cairo", "washington"]

    ask = random.choice(cities)
    url = f'https://api.openweathermap.org/data/2.5/weather?q={ask}&appid=36f60923963562f679d4d6043a270088'

    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    temp_c = result['main']['temp'] - 273.25
    temp_f = (result['main']['temp'] - 273.15) * 9 / 5 + 32

    print("You look up and see", result["weather"][0]["description"])