import requests
from pprint import pprint

API_Key = '1fe88a1abf846ab205dc08a9bc0bccba'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+ API_Key + "&q=" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
