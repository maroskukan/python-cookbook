#!/usr/bin/env python


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # Recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # Perform the merging
        i = 0
        j = 0
        k = 0
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # Check if left array still has values and add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # Check if right array still has values and add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

    return dataset


if __name__ == "__main__":
    print(items)
    mergesort(items)
    print(items)
