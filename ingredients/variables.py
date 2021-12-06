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

