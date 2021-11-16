#!/usr/bin/env python

# define a set of items that we want to count items for type
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

# Create a new hash table object to hold the items and counts
counter = dict()

# Iterate over each item and increment the count for each one
for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

# print the result
print(counter)
