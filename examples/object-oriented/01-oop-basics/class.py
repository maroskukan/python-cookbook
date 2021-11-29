class Book:
    # properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __booklist = None

    # create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype


# access the class attribute
print("Book types: ", Book.getbooktypes())

# create some book instances
b1 = Book("The Grapes of Wrath", "HARDCOVER")
b2 = Book("The Catcher In The Rye", "PAPERBACK")
try:
    b3 = Book("A Tale of Two Cities", "COMIC")
except ValueError as err:
    print(err)
finally:
    b3 = Book("A Tale of Two Cities", "HARDCOVER")

# use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
thebooks.append(b3)

print(thebooks)
