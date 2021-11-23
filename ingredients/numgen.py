#!/usr/bin/env python

# Generate file with numbers from 00000000 999999999
# Resulting file size is ~9.3GB


def main():
    # Open a file for writing and create it if it does not exists
    f = open("numbers_8-9.txt", "w+")

    # write some lines of data to the file
    for i in range(1000000000):
        f.write(str(i).zfill(8) + "\n")

    # Close the file when done
    f.close()


if __name__ == "__main__":
    main()
