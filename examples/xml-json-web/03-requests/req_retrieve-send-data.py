#!/usr/bin/env python

import requests


def main():
    # Use requests to send a GET request to the URL
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    printResult(result)

    # Send some parameters to the URL via a GET request
    url = "http://httpbin.org/get"
    args = {"name": "Maros", "is_author": True}
    result = requests.get(url, params=args)
    printResult(result)

    # Send some parameters to the URL via a POST request
    url = "http://httpbin.org/post"
    form = {"name": "Maros", "is_author": True}
    result = requests.post(url, data=form)
    printResult(result)

    # Send some parameters to the URL via a GET custom headers
    url = "http://httpbin.org/get"
    headerValues = {"User-agent": "Googlebot"}
    result = requests.get(url, headers=headerValues)
    printResult(result)


def printResult(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: {0}".format(resData.headers))
    print("\n")

    # print("Returned data: {0}".format(resData.content))
    print("Returned data: {0}".format(resData.text))


if __name__ == "__main__":
    main()
