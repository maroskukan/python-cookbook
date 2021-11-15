#!/usr/bin/env python


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x - 1)
        print("foo")


countdown(5)
