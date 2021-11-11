#!/usr/bin/env python

# Create a hashtable all at once
items1 = dict({"one": 1, "two": 2, "three": 3})
print(items1)

# Create a hashtable progressively
items2 = {}
items2["one"] = 1
items2["two"] = 2
items2["three"] = 3
print(items2)

# Try to access a nonexistent key
try:
    print(items2["four"])
except KeyError:
    print("KeyError: 'four'")

# Replace an item
items2["one"] = "uno"
print(items2)

# Iterate over all keys and values in the dictionary
for key, value in items2.items():
    print(f"Key: {key} Value: {value}")
