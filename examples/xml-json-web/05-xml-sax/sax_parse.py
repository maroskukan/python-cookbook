#!/usr/bin/env python

import requests
import xml.sax


class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    # handle startElement
    def startElement(self, tagName, attrs):
        if tagName == "slideshow":
            print("Slideshow title: " + attrs["title"])
        elif tagName == "slide":
            self.slideCount += 1
        elif tagName == "item":
            self.itemCount += 1
        elif tagName == "title":
            self.isInTitle = True

    # handle endElement
    def endElement(self, tagName):
        if tagName == "title":
            self.isInTitle = False

    # handle text data
    def characters(self, chars):
        if self.isInTitle:
            print("Title: " + chars)

    # handle startDocument
    def startDocument(self):
        print("About to start")

    # handle endDocument
    def endDocument(self):
        print("Finished")


def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    # use the Request lib to get XML data from the server
    # requests auto-decodeds our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    # print(result.text)

    # call the parseString method on the XML text content received
    xml.sax.parseString(result.text, handler)

    # print some interesting results
    print("There were {0} slide elements".format(handler.slideCount))
    print("There were {0} item elements".format(handler.itemCount))


if __name__ == "__main__":
    main()
