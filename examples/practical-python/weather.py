import json
import urllib.request
import urllib.parse
import os


def get_weather_data():
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
            return {'city': city,
                    'description': description,
                    'temp_min': temp_min,
                    'temp_max': temp_max}
        else:
            return None
    except Exception:
            return None


def main():
    weather_dict = get_weather_data()
    if weather_dict:
        print(f"Today forecast for {weather_dict.get('city')} is {weather_dict.get('description')}.\n")
        print(f"Minimum temperature is {weather_dict.get('temp_min')}°C")
        print(f"Maximum temperature is {weather_dict.get('temp_max')}°C")
    else:
        print(f"Unable to load weather data.")

main()