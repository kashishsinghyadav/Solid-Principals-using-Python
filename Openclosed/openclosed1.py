from abc import ABC, abstractmethod 

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order(ABC):
    @abstractmethod
    def calculate(self):
        pass  

class StandardOrder(Order):
    def __init__(self, items):
        self.items = items

    def calculate(self):
        total = [item.price for item in self.items]
        return sum(total)

class DiscountOrder(Order):
    def __init__(self, disrate, items):
        self.items = items
        self.disrate = disrate 

    def calculate(self):
        total = [item.price for item in self.items]
        return sum(total) * (1 - self.disrate)
    
standard_items = [Item('skrit', 10), Item('cargo', 20), Item('tee', 60)]
obj1 = StandardOrder(standard_items)
print('The standard order total is:', obj1.calculate())

discount_items = [Item('contour', 60), Item('primer', 100), Item('tint', 40)]
obj2 = DiscountOrder(0.2, discount_items)
print('The total amount after discount is:', obj2.calculate())
