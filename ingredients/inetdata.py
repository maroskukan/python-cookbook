#!/usr/bin/env python

import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    date = webUrl.read()
    print(date)


if __name__ == "__main__":
    main()
