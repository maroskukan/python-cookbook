#!/usr/bin/env python

# use a hash table to filter out duplicate elements

# define a set of items that we want to reduce duplicates
items = [
    "apple",
    "pear",
    "orange",
    "banana",
    "apple",
    "orange",
    "apple",
    "pear",
    "banana",
    "orange",
    "pear",
    "banana",
    "apple",
    "kiwi",
    "pear",
]

# crete a hash table
filter = dict()

# loop over the items and add to the hash table
for key in items:
    filter[key] = 0

# create a set from the resulting keys
result = set(filter.keys())

print(result)
