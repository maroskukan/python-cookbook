#!/usr/bin/env python

import urllib.request
import json
import os


def printResults(data):
    term_size = os.get_terminal_size()
    # use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # now we can access the contents of the JSON like any other Python objects
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    # output the number of events, plus the magnitured and each event name
    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    # for each event, print the place where it occured
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print(str("-" * term_size.columns + "\n"))

    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print(str("-" * term_size.columns + "\n"))

    # print only the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(
                    "%2.1f" % i["properties"]["mag"],
                    i["properties"]["place"],
                    " reported " + str(feltReports) + " times",
                )
    print(str("-" * term_size.columns + "\n"))


def main():
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))

    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")


if __name__ == "__main__":
    main()
