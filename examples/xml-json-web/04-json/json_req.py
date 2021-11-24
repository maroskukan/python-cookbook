#!/usr/bin/env python

import requests
from requests import HTTPError, Timeout
import json
from json import JSONDecodeError


def main():
    # Use requests to issues a GET request to the URL
    try:
        url = "http://httpbin.org/json"
        result = requests.get(url, timeout=2)
        result.raise_for_status()

        # Use built-in JSON decoder to convert the JSON string into a Python object
        try:
            dataobj = result.json()
            print(json.dumps(dataobj, indent=4))

            # Print the data root level keys list
            print(list(dataobj.keys()))

            try:
                print((dataobj["slideshow"]["title"]))
                print(
                    "There are {0} slides".format(len(dataobj["slideshow"]["slides"]))
                )
            except KeyError:
                print("No title found")

        except JSONDecodeError as err:
            print("JSON decode error")
            print(err)

    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request timed out: {0}".format(err))


if __name__ == "__main__":
    main()
