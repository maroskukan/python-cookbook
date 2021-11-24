#!/usr/bin/env python

import requests
from requests.auth import HTTPBasicAuth


def main():
    # Access a URL that requires authentication.
    url = "http://httpbin.org/basic-auth/user/pass"

    # create a credentials object using HTTPBasicAuth
    credentials = HTTPBasicAuth("user", "pass")

    # Issue the request, with the credentials using object or pass directly
    # result = requests.get(url, auth=credentials)
    result = requests.get(url, auth=("user", "pass"))

    printResults(result)


def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Returned data: -----------------")
    print(resData.text)


if __name__ == "__main__":
    main()
