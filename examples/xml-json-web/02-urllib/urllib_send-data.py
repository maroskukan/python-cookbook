#!/usr/bin/env python

import urllib.request
import urllib.parse


def main():
    url = "http://httpbin.org/get"

    # create some to pass to the GET request
    args = {"name": "Maros", "is_author": True}

    # encode the parameters for the request
    data = urllib.parse.urlencode(args)

    # create a request object
    # response = urllib.request.urlopen(url + "?" + data)

    # issue the request with a data parameter to use POST
    url = "http://httpbin.org/post"
    payload = data.encode()
    response = urllib.request.urlopen(url, data=payload)

    print("Response code: {0}".format(response.status))
    print("Returned data: {0}".format(response.read().decode("utf-8")))


if __name__ == "__main__":
    main()
