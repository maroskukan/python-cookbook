class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        # add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


# create some books instances
b1 = Book("Brave New World", "Aldous Huxley", 200, 25.00)
b2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 400, 35.00)

# print the price of book1
print(b1.getprice())

# try setting a discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# properties with double underscores are hidden by the interpreter
try:
    print(b2.__secret)
except AttributeError as err:
    print(err)

try:
    print(b2._Book__secret)
except AttributeError as err:
    print(err)
