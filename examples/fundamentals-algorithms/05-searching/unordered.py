#!/usr/bin/env python

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        if item == itemlist[i]:
            return i

    return None


print(find_item(87, items))
print(find_item(250, items))
