#!/usr/bin/env python


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


if __name__ == "__main__":
    main()
