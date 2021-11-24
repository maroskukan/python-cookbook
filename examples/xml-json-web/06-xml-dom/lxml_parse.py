#!/usr/bin/env python

import requests
from lxml import etree

def main():
    # retrueve the XML data from the server
    url = "http://httpbin.org/xml"
    result = requests.get(url)

    # build a doc structure using the ElementTree API
    doc = etree.fromstring(result.content)

    # access the value of an attribute
    print(doc.tag)
    print(doc.attrib["title"])


    # iterate over tags
    for elem in doc.findall("slide"):
        print(elem.tag)

    slideCount = len(doc.findall("slide"))
    print("There are {0} slide elements".format(slideCount))

    # create a new slide
    newSlide = etree.SubElement(doc,"slide")
    newSlide.text = "New slide text"

    # count the number of slides
    slideCount = len(doc.findall("slide"))
    itemCount = len(doc.findall(".//item"))

    print("There are {0} slide elements".format(slideCount))
    print("There are {0} item elements".format(itemCount))


if __name__ == "__main__":
    main()