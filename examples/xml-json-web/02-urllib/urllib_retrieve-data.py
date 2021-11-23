#!/usr/bin/env python

import urllib.request


def main():
    # the URL to retrieve our sample data from
    url = "http://httpbin.org/xml"

    # open the URL and read the data
    response = urllib.request.urlopen(url)

    # print the response code from the request, should be 200 OK
    print("Response code: {0}".format(response.status))

    # print the response headers
    print("Response headers: {0}".format(response.getheaders()))

    # print the response data (raw data in bytes)
    print("Response data: {0}".format(response.read().decode("utf-8")))


if __name__ == "__main__":
    main()
