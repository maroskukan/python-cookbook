#!/usr/bin/env python

import json
from json import JSONDecodeError


def main():
    jsonStr = """{
        "sandwich": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ]
        "price": 8.99
    }"""

    try:
        # parse the JSON data using loads (load string)
        data = json.loads(jsonStr)
        # print information from the data
        print("Sandwich: " + data["sandwich"])
        if data["toasted"]:
            print("Toasted: Yes")
        for topping in data["toppings"]:
            print("Served with: " + topping)
    except JSONDecodeError as err:
        print("JSON decode error")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == "__main__":
    main()
