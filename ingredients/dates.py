#!/usr/bin/env python

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is ", today)

    # Print out date's individual components
    print("Date components: ", today.day, today.month, today.year)

    # Retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday number is: ", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

    print("Which day is today:", days[today.weekday()])

    # Get current date and time from now() method from teh datetime class
    now = datetime.now()
    print("The current date and time is", now)

    # Get current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()
