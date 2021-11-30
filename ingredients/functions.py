#!/usr/bin/env python

# define a basic function
def func1():
    print("I am a fucntion")


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return x * x * x


# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


func1()  #  Direct call
print(func1())  # Wrapped within print()
print(func1)  # Prints function address

func2(10, 20)
print(func2(10, 20))
print(cube(3))

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

print(multi_add(1, 2, 3, 4, 5))

# define a global variable
cheese = "cheddar"

# create a generic mix and cook function
def mix_and_cook():
    print("Mixing the ingredients")
    print("Pouring the mixture into a frying pan")
    print("Cooking the omelette for 5 minutes")
    print("Enjoy!")


# leverage existing function and global variable if local is not defined
def make_omelete():
    mix_and_cook()
    omellete = f"A teasty {cheese} Omelette"
    return omellete


# manimulate a global variable from function
def make_pancake():
    mix_and_cook()
    global cheese
    cheese = "swiss"
    pancake = f"A delicious {cheese} pancake"
    return pancake


# create a function that takes variable number of arguments
def fancy_omelette(*ingredients):
    mix_and_cook()
    omellete = f"A fancy omelette with {len(ingredients)} ingredients"
    return omellete


omelette2 = fancy_omelette("cheese", "tomato", "egg")
pancake = make_pancake()
omelette1 = make_omelete()

print(omelette1)
print(omelette2)
print(pancake)
