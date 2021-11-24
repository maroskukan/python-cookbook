#!/usr/bin/env python

import json


def main():
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": ["Tousand Island Dressing", "Sauerkraut", "Pickles"],
        "price": 8.99,
    }

    # convert the Python object into a JSON string
    jsonStr = json.dumps(pythonData, indent=4)

    # print the resulting JSON string
    print(jsonStr)


if __name__ == "__main__":
    main()
