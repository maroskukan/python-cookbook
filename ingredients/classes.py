#!/usr/bin/env python


class myClass:
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print(f"myClass method2 {someString}")


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2")


class jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print(f"Puttin on {self.waist}x{self.length} {self.color} jeans")
        self.wearing = True

    def take_off(self):
        print(f"Taking off {self.waist}x{self.length} jeans")
        self.wearing = False


class shirt:
    def __init__(self):
        self.clean = True

    def make_dirty(self):
        self.clean = False

    def make_clean(self):
        self.clean = True


class Vehicle:
    def __init__(self, color, manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4  # Full tank of gas

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print(f"The {self.color} {self.manuf} goes vroom!")
        else:
            print(f"The {self.color} {self.manuf} is out of gas.")

    def fill_gas(self):
        self.gas = 4


class Car(Vehicle):
    def radio(self):
        print("Rockin' the tunes")

    def window(self):
        print("Looking out the window")


class Motorcycle(Vehicle):
    def helmet(self):
        print("Putting on helmet")


class eCar(Car):
    def drive(self):
        print(f"The {self.color} {self.manuf} goes ssshhhhh!")


def main():
    a = myClass()
    a.method1()
    a.method2("This is a string")

    b = anotherClass()
    b.method1()
    b.method2("This is a string")

    jeans1 = jeans(34, 34, "blue")

    jeans1.put_on()
    print(f"Jeans1 is wearing: {str(jeans1.wearing)}")
    jeans1.take_off()
    print(f"Jeans1 is wearing: {str(jeans1.wearing)}")

    shirt1 = shirt()
    shirt2 = shirt()
    shirt1.make_dirty()
    print(f"Shirt1 is clean: {str(shirt1.clean)}")
    print(f"Shirt2 is clean: {str(shirt2.clean)}")

    shirt1.make_clean()
    print(f"Shirt1 is clean: {str(shirt1.clean)}")

    car1 = Car("red", "Ford")
    car1.radio()
    car1.drive()

    motorcycle1 = Motorcycle("blue", "Honda")
    motorcycle1.helmet()


if __name__ == "__main__":
    main()
