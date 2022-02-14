import datetime
import csv
import random
from urllib import request
import json
from webbrowser import get
import tweepy
import os


"""
Retrieve a random quote from the specifid CSV file.
"""


def get_random_quote(quotes_file="quotes.csv"):
    try:  # load motivational quotes from csv file
        with open(quotes_file) as csvfile:
            quotes = [
                {"author": line[0], "quote": line[1]}
                for line in csv.reader(csvfile, delimiter="|")
            ]
    except Exception as e:  # use a default quote to help things to turn out for the best
        quotes = [
            {"author": "Eric Idle", "quote": "Always Look on the Bright Side of Life."}
        ]

    return random.choice(quotes)


"""
Retrieve the current weather forecast from OpenWeatherMap.
"""


def get_weather_forecast(
    coords={"lat": 28.4717, "lon": -80.5378}
):  # default location at Cape Canaveral
    try:  # retrieve forecast for specified coordinates
        api_key = os.environ.get(
            "OW_API_KEY"
        )  # load OpenWeatherMap API key from environment variable
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&units=metric&appid={api_key}'
        data = json.load(request.urlopen(url))

        forecast = {
            "city": data["city"]["name"],  # city name
            "country": data["city"]["country"],  # country name
            "periods": list(),  # list to hold forecast data for future periods
        }

        for period in data["list"][0:9]:  # pupulate list with next 9 forecast periods
            forecast["periods"].append(
                {
                    "timestamp": datetime.datetime.fromtimestamp(period["dt"]),
                    "temp": round(period["main"]["temp"]),
                    "description": period["weather"][0]["description"].title(),
                    "icon": f'http//openweathermap.org/img/wm/{period["weather"][0]["icon"]}.png',
                }
            )
        return forecast

    except Exception as e:
        print(f"\nWeather forecast not available.")


"""
Retrieve the current trends from Twitter.
"""


def get_twitter_trends(woeid=23424977):  # default WOEID for United States
    try:  # retrieve Twitter trends for specified location
        api_key = os.environ.get(
            "TWT_API_KEY"
        )  # load Twitter API key from environment variable
        api_secret_key = os.environ.get(
            "TWT_SECRET_KEY"
        )  # load Twitter Secret key from environment variable
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        return tweepy.API(auth).get_place_trends(woeid)[0]["trends"]

    except Exception as e:
        print(e)


def get_wikipedia_article():
    """
    Retrieve the summary extract for a random Wikipedia article
    """
    try:  # retrieve random Wikipedia article
        data = json.load(
            request.urlopen("https://en.wikipedia.org/api/rest_v1/page/random/summary")
        )
        return {
            "title": data["title"],
            "extract": data["extract"],
            "url": data["content_urls"]["desktop"]["page"],
        }
    except Exception as e:
        print(e)


if __name__ == "__main__":
    ##### test get_random_quote() #####
    print(("\nTesting quote generation..."))

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" by {quote["author"]}')

    quote = get_random_quote(quotes_file=None)
    print(f' - Default quote is "{quote["quote"]}" by {quote["author"]}')

    ##### test get_weather_forecast() #####
    print(("\nTesting weather forecast retrieval..."))

    forecast = get_weather_forecast()  # get forecast for default location
    if forecast:
        print(f'nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast["periods"]:
            print(
                f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}'
            )

    slovakia = {
        "lat": 49.1666,
        "lon": 20.1316,
    }  # coordinates for Novy Smokovec, Slovakia
    forecast = get_weather_forecast(
        coords=slovakia
    )  # get forecast for Novy Smokovec, Slovakia
    if forecast:
        print(f'\nWeather forecast for {forecast["city"]}, {forecast["country"]} is...')
        for period in forecast["periods"]:
            print(
                f' - {period["timestamp"]} | {period["temp"]}°C | {period["description"]}'
            )

    invalid = {"lat": 1234.5678, "lon": 1234.5678}  # invalid coordinates
    forecast = get_weather_forecast(
        coords=invalid
    )  # get forecast for invalid coordinates
    if forecast is None:
        print("Weather forecast for invalid coordinates returned None")

    ##### test get_twitter_trends() #####
    print("\nTesting Twitter trends retrieval...")

    trends = get_twitter_trends()  # get trends for default location of United States
    if trends:
        print("\nTop 10 Twitter trends in the United States are...")
        for trend in trends[0:10]:  # show top ten
            print(f' - {trend["name"]}: {trend["url"]}')

    trends = get_twitter_trends(woeid=44418)  # get trends for London
    if trends:
        print("\nTop 10 Twitter trends in London are...")
        for trend in trends[0:10]:  # show top ten
            print(f' - {trend["name"]}: {trend["url"]}')

    trends = get_twitter_trends(woeid=-1)  # invalid WOEID
    if trends is None:
        print("Twitter trends for invalid WOEID returned None")

    ##### test get_wikipedia_article() #####
    print("\nTesting random Wikipedia article retrieval...")

    article = get_wikipedia_article()
    if article:
        print(f'\n{article["title"]}\n<{article["url"]}>\n{article["extract"]}')
