#!/usr/bin/env python

from datetime import date
import calendar


def main():
    x, y = 10, 100
    if x < y:
        st = "x is less than y"
    elif x == y:
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print(st)

    # conditional statements let you use a "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater or same as y"
    print(st)

    # ordering a pizza example
    diet_restrictions = set(["meat", "cheese"])

    # Cheese pizza will be selected
    # in order to fix it more specific conditions should be on top
    if "meat" in diet_restrictions:
        print("Get a chesse pizza.")
    elif "meat" and "cheese" in diet_restrictions:
        print("Get a vegan pizza.")
    else:
        print("Get something else.")

    # Simulate switch and case statements
    specials = {
        "Monday": "spinach",
        "Tuesday": "mushrooms",
        "Wednesday": "tomatoes",
        "Thursday": "cheese",
        "Friday": "pepperoni",
        "Saturday": "chicken",
        "Sunday": "eggs",
    }

    def order(day):
        if day in specials:
            print("Today's special is {}".format(specials[day]))
        else:
            print("No special today.")

    # Get the name of the day and used that as an argument
    today = calendar.day_name[date.today().weekday()]
    order(today)


if __name__ == "__main__":
    main()
