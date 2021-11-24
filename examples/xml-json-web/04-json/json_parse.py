#!/usr/bin/env python

import json


def main():
    # define a string of JSON code
    jsonStr = """{
        "sandwich": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price": 8.99
    }"""

    # parse the JSON string into a Python object (dictionary)
    data = json.loads(jsonStr)

    # print the object
    print("Sandwich: " + data["sandwich"])

    if data["toasted"]:
        print("Toasted: Yes")
    if data["toppings"]:
        print("Served with: ")
        for topping in data["toppings"]:
            print(topping)


if __name__ == "__main__":
    main()
