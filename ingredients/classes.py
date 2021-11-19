#!/usr/bin/env python


class myClass:
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2")


def main():
    a = myClass()
    a.method1()
    a.method2("This is a string")

    b = anotherClass()
    b.method1()
    b.method2("This is a string")


if __name__ == "__main__":
    main()
