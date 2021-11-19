#!/usr/bin/env python


def main():
    # Open a file for writing and create it if it does not exists
    # f = open("textfile.txt", "w+")

    # Open the file for appending text to the end
    f = open("textfile.txt", "a")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")

    # Close the file when done
    f.close()

    # Open the file back up and read the contents
    f = open("textfile.txt", "r")
    if f.mode == "r":
        #contents = f.read()
        fl = f.readlines()
        for x in fl:
            print(x)
    #print(contents)



if __name__ == "__main__":
    main()
