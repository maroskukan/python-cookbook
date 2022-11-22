import json
import urllib.request
import urllib.parse
import os

try:
    api_key = os.environ['WEATHER_API_KEY']
except Exception as e:
    print(f"Unable to retrieve value from {str(e)} variable")
    quit()

city = input("Please enter the city name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city)}&appid={api_key}&units=metric'

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    if data['cod'] == 200:
        description = data['weather'][0]['description']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        print(f"Today forecast for {city} is {description}.\n")
        print(f"Minimum temperature is {temp_min}")
        print(f"Maximum temperature is {temp_max}")
    else:
        print('The response does not contain valid data.')
except Exception as e:
    print(f"Unable to load data. {str(e)}")