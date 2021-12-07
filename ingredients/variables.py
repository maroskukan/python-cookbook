#!/usr/bin/env python

# Declare a variable and initialize it
f = "0"
print(f)

# Re-declare a variable
f = "abc"
print(f)


# Using Docstring to create list
autobots = """
Optimus Prime
Bumblebee
Cliffjumper
Jazz
Cliffjumper
Wheeljack
Prowl
""".split()

# Global vs local variables in functions
def someFunction():
    global f
    f = "def"
    print(f)


someFunction()
print(f)

# Deleting a variable
del f
try:
    print(f)
except NameError:
    print("f is undefined")

# Define a multidiemensional list
lot_2d = [["Toyota", "Audi", "BMW"], ["Honda", "Nissan", "Ford"], ["Lexus", "Jeep"]]

lot_3d = [
    [["Toyota", "Audi", "BMW"], ["Honda", "Jeep"], ["Saab", "Kia", "Ford"]],
    [["Subaru", "Nissan"], ["Volvo"]],
    [["Mazda", "Chevy"], [], ["Volkwagen"]],
]

# Access elements in a list
print(lot_2d[0][0])
print(lot_2d[2][1])
print(lot_3d[0][0][0])
print(lot_3d[0][0][2])

for floor in lot_3d:
    for row in floor:
        for car in row:
            print(car)

# Creating and Combining Sets of Friends

collage = set(["Bill", "Katy", "Verne", "Dillon" "Bruce", "Olivia", "Richard", "Jim"])
coworkers = set(
    ["Aaron", "Bill", "Brandon", "David", "Frank", "Connie", "Kyle", "Olivia"]
)
family = set(["Garry", "Landon", "Larry", "Mark", "Olivia", "Katy", "Rae", "Tom"])

# Count objects in a set
noColl = len(collage)
noCowo = len(coworkers)
noFami = len(family)

# Single set of all friends
friends = collage.union(coworkers, family)

# Sorting Friends into Sets

# set of all friends
friends = set(
    [
        "Mark",
        "Rae",
        "Verne",
        "Richard",
        "Aaron",
        "David",
        "Bruce",
        "Garry",
        "Bill",
        "Connie",
        "Larry",
        "Jim",
        "Landon",
        "Dillon",
        "Frank",
        "Tom",
        "Kyle",
        "Katy",
        "Olivia",
        "Brandon",
    ]
)

# set of people who live in my zip code
zipcode = set(
    [
        "Jerry",
        "Eleine",
        "Cindy",
        "Verne",
        "Rudolph",
        "Bill",
        "Olivia",
        "Jim",
        "Lindsay",
        "Rae",
        "Mark",
        "Kramer",
        "Landon",
        "Newman",
        "George",
    ]
)

# set of people who play Munchkin
munchkins = set(["Steve", "Jackson", "Frank", "Bill", "Mark", "Landon", "Rae"])

# set of Olivia's friends
olivia = set(["Jim", "Amanda", "Verne", "Nestor"])

local = friends.intersection(zipcode)
invite = local.difference(munchkins)
munchkins.difference(local)
invite = invite.symmetric_difference(olivia)

# Check if item exists in set
verne_present = "Verne" in invite

# Add item to a set
invite.add("Verne")

# Remove item from set
invite.remove("Nestor")

# Return item form set
removed = invite.pop()
