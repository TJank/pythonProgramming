

# Problem 1.
class Book(object):
    def __init__(self, title, author, publisher, price, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price
        self.ISBN = isbn

    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getPublisher(self):
        return self.publisher
    def getPrice(self):
        return self.price
    def getISBN(self):
        return self.ISBN



# Problem 2.
class ShoppingCart(object):
    def __init__(self):
        self.items = []
        self.prices = []
        self.total = 0

    def getItems(self):
        return self.items

    def getPrices(self):
        return self.prices

    def addItem(self, itemName, price):
        self.items.append(itemName)
        self.prices.append(price)

    def removeItem(self, itemName):
        indx = self.items.index(itemName)
        self.items.pop(indx)
        self.prices.pop(indx)

    def totalPrice(self):
        for i in range(len(self.prices)):
            self.total += self.prices[i]

        return self.total



# Problem 3.



# Problem 4.


# Problem 5.