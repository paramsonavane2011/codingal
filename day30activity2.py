class Computer():
    def __init__(self):
        self.__maxPrice = 69
    def price(self):
        print(self.__maxPrice)
    def setMaxPrice(self, price):
        self.__maxPrice = price
    
com = Computer()
com.price()
com.setMaxPrice(70)
com.price()
com.__maxPrice = 71
com.price()
