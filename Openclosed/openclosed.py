#1. using inheritance/abstract class
#2. composition/injection
#3.parameter/arguments 

from abc import ABC,abstractmethod 
class Shape(ABC):# python not support interface so we used abstractclass+ multiple inheritance 
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2 
    
class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath

    def area(self):
        return self.length*self.breath 
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius 
    def area(self):
        return 3.14*self.radius*self.radius 
    
obj1=Square(10)
print("the area of square is",obj1.area())
obj2=Rectangle(5,3)
print("The area of Rectange is ",obj2.area())
obj3=Circle(6)
print("The area of circle is ",obj3.area())



