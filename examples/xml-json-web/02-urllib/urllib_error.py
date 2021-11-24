#!/usr/bin/env python

import urllib.request
from urllib.error import HTTPError, URLError
from http import HTTPStatus


def main():
    url = "http://no-such-server.org"  # will generate a URLError
    # url = "http://httpbin.org/status/404"  # will generate an HTTPError
    # url = "http://httpbin.org/html"  # should work with no errors

    try:
        response = urllib.request.urlopen(url)

        print("Response cpde: {0}".format(response.status))
        if response.getcode() == HTTPStatus.OK:
            print(response.read().decode("utf-8"))
    except HTTPError as err:
        print("Error: {0}".format(err.code))
    except URLError as err:
        print("Error: {0}".format(err.reason))


if __name__ == "__main__":
    main()
