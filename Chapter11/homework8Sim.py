from homework8 import *

myCart = ShoppingCart()
myCart.addItem("4k TV", 1000)
myCart.addItem("Ipod", 300)
myCart.addItem("Speaker Set", 250)
myCart.addItem("Movie", 20)
print(myCart.getItems())
print(myCart.getPrices())
myCart.removeItem("Ipod")
print(myCart.getItems())
print(myCart.getPrices())
print(myCart.totalPrice())




