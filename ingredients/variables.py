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
print(f)
