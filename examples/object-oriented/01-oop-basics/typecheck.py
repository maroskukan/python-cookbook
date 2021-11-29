class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The New York Times")
n2 = Newspaper("The Wall Street Journal")

# use type() to inspect the type of an object
print(type(b1))
print(type(n1))

# compare the types of the objects
print(type(b1) == type(b2))  # True
print(type(b1) == type(n1))  # False

# use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))  # True
print(isinstance(n1, Book))  # False
print(isinstance(n1, Newspaper))  # True
print(isinstance(b1, object))  # True
