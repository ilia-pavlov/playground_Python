"""class Product:

    def __init__(self, price):
        # self.__price = price
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value

    price = property(get_price, set_price)
"""
class Product:

    def __init__(self, price):
        # self.__price = price
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value


product = Product(10)
product.price = -1
print(product.price)