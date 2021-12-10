#!/usr/bin/env python

import random


def main():
    x = 0

    # define a while loop
    # while x < 5:
    #     print(x)
    #     x += 1

    # define a for loop
    for x in range(5, 10):
        print(x)

    # define a list of days in week
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # use break and continue statement
    for y in range(5, 10):
        if y % 2 == 0:
            continue
        print(y)
        # if y == 7:
        #     break
        # print(y)

    # define a list of months in a year
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]

    for i, m in enumerate(months):
        print("Index", i, "Value", m)

    # dirty dishes in the sink
    sink = ["bowl", "cup", "plate", "fork", "knife"]

    # iterate over the new sink list, print each item and remove dish from original list
    for dish in list(sink):
        print(f"Putting {dish} in the dishwasher")
        sink.remove(dish)

    # print the sink list
    print(sink)

    # scrubbing a stuborn pan
    dirty = True
    scrub_count = 0

    while dirty:
        scrub_count += 1
        print(f"Scrub the pan: {scrub_count}")

        print("Rinse & check if the pan is clean.")
        if not random.randint(0, 9):
            print("Pan is clean!")
            dirty = False
        else:
            print("Still dirty...")

        # Statement below always runs
        print("...")

    # putting away clean dishes
    dishwasher = [
        "plate",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "cup",
        "spatula",
        "ladle",
        "saucepan",
        "cup",
        "spatula",
        "ladle",
        "saucepan",
        "cup",
        "plate",
        "fork",
        "knife",
        "spoon",
        "bowl",
        "cup",
    ]

    # iterate over the new dishwasher list, break from loop if randint returns 0
    for dish in list(dishwasher):
        if not random.randint(0, 19):
            print("Out of space!")
            break
        else:
            print(f"Putting {dish} in the cabinet")
            dishwasher.remove(dish)


if __name__ == "__main__":
    main()
