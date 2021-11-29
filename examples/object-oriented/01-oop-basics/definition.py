# create a basic class
class Book:
    def __init__(self, title):
        self.title = title


# create instances of the class
b1 = Book("Brave New World")
b2 = Book("The Lord of the Rings")

# print the class and property
print(b1)
print(b1.title)
