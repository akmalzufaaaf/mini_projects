import requests

API_KEY = "02d29883ef479fc40b87db020c13f6c6"
BASE_URL_FOR_GEOCODING = "http://api.openweathermap.org/geo/1.0/direct"
BASE_URL_FOR_WEATHER = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

# Get coordinate of input city/country
TheCoord_URL = f"{BASE_URL_FOR_GEOCODING}?appid={API_KEY}&q={city}" # Coord : Coordinate
responseForCoord = requests.get(TheCoord_URL)
if responseForCoord.status_code == 200:
    data = responseForCoord.json()
    lat = data[0]["lat"]
    lon = data[0]["lon"]
else:
    print("Error is occured")

# Get weather information in selected city/country
request_url_for_weather = f"{BASE_URL_FOR_WEATHER}?lat={lat}&appid={API_KEY}&lon={lon}"
responseForWeather = requests.get(request_url_for_weather)
if responseForWeather.status_code == 200:
    data = responseForWeather.json()
    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'] - 273.15, 2)
    print(f"{city} is {weather} now")
    print(f"and it's about {temp}°celsius")
else:
    print("Error occured")
    
