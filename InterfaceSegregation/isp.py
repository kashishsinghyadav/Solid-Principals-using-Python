#The Interface Segregation Principle (ISP) states that clients should not be forced to depend on interfaces they do not use. In other words, it's better to have many small, specific interfaces rather than a few large, general ones.
from abc import ABC,abstractmethod 

class Renderable(ABC):
    @abstractmethod
    def render(self):
        pass 
class Clicable(ABC):
    @abstractmethod
    def handleclick(self):
        pass 
class Tyable(ABC):
    @abstractmethod 
    def handlekeypress(self):
        pass 

class Button(Renderable,Clicable):
    def render(self):
        return " Button also render into another page" 
    def handleclick(self):
        return "Button can also used for click"
    
class TextField(Renderable,Tyable):
    def handlekeypress(self):
        return "Typing in textfield"
    def render(self):
        return " Text link also render into another page"  
class Label(Renderable):
    def render(self):
        return "Rendering label"
    
objb=Button()
print(objb.render())
print(objb.handleclick())
print()
objt=TextField()
print(objt.handlekeypress())
print(objt.render()) 
print()
objl=Label()
print(objl.render())


