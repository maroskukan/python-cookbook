#!/usr/bin/env python

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # create a backup copy by appending ".bak" to thge name
        dst = src + ".bak"

        # copy over the permissions, modificaiton times, and other info
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        # rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        # Put all items into a ZIP archive
        root_dir, _ = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.zip.bak")


if __name__ == "__main__":
    main()
