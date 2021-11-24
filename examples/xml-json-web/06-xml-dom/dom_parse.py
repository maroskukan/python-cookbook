#!/usr/bin/env python

import xml.dom.minidom
import requests


def main():
    url = "http://httpbin.org/xml"
    result = requests.get(url)

    # parse the returned content into a DOM structure
    domtree = xml.dom.minidom.parseString(result.text)
    rootnode = domtree.documentElement

    # display some information about the content
    print("Root element is: {0}".format(rootnode.nodeName))
    print("Title: {0}".format(rootnode.getAttribute("title")))

    items = rootnode.getElementsByTagName("item")
    print("There are {0} item tags".format(items.length))

    # manipulate the XML content in memory
    # create a new item tag
    newItem = domtree.createElement("item")

    # add some text to the item
    newItem.appendChild(domtree.createTextNode("New item text"))

    # add the item to the first slide
    firstSlide = domtree.getElementsByTagName("slide")[0]
    firstSlide.appendChild(newItem)

    # count the item tags again
    items = rootnode.getElementsByTagName("item")
    print("There are {0} item tags".format(items.length))


if __name__ == "__main__":
    main()
