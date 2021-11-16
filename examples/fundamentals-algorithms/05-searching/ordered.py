#!/usr/bin/env python

# Create an ordered list of random numbers
items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # calculate the middle point
        midpoint = (lowerIdx + upperIdx) // 2

        # if item is found at the middle point
        if itemlist[midpoint] == item:
            return midpoint

        # otherwise get the next midpoint
        if item > itemlist[midpoint]:
            lowerIdx = midpoint + 1
        else:
            upperIdx = midpoint - 1

    if lowerIdx > upperIdx:
        return None


if __name__ == "__main__":
    print(binarysearch(23, items))
    print(binarysearch(87, items))
    print(binarysearch(250, items))
