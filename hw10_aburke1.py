# Alexandra Burke
# Homework 10 

class Product():
    
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__inventory = quantity 
        self.__price = price
    
    def getName(self):
        return self.__name

    def getInventory(self):
        return self.__inventory

    def getPrice(self):
        return self.__price

    def setName(self, name):
        self.__name = name
    
    def setInventory(self, price):
        self.__inventory = quantity 

    def setPrice(self, price):
        self.__price = price
    
    def make_purchase(self, quantity):
        if quantity > self.__inventory:
            print('Error')
        else: 
                self.__inventory -= quantity 
                total_price = quantity * self.__price
                if quantity < 10:
                    discount = 0
                elif quantity <= 99:
                    discount = 10
                else:
                    discount = 20
            
                print('Amount bought: ', quantity)
                print('Price: ${:.2f} '.format(total_price*(100 - discount)/100))
                print('Discount: ', discount)
                print('Inventory: ', self.__inventory)
        
def __str__(self):
    return f'Name: {self.__name}, Stock: {self.__inventory}, Price: ${self.__price:.2f}'

apple = Product('apple', 1000,10)
print(apple)
amount = [7,530,480,243]
for quantity in amount: 
    apple.make_purchase(quantity)
    print()
    