#!/usr/bin/env python

from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encoutered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        if tag == "meta":
            global metacount
            metacount += 1
        print("Encoutered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print(("\t", a[0], "=", a[1]))

    def handle_endtag(self, tag):
        print("Encoutered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encoutered data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)
    print("Meta tags found: " + str(metacount))


if __name__ == "__main__":
    main()
