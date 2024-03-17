#The principle defines that objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.

from abc import ABC, abstractmethod 

class Vehicle(ABC):# --> we have vehicle class which having the the function haswheel which is comman for all the class either the vehicle has engine or not but if we add has engine in this class it may happen for bicycle class it gives the null values which violates the lsp 
    @abstractmethod
    def has_wheel(self):
        pass

class VehicleWithEngine(Vehicle):# created the class which having the object which having the engine and it inherit by all the class which have the same method and behvaiour
    def has_engine(self):
        return True

class Car(VehicleWithEngine):
    def has_engine(self):
        return True
    def has_wheel(self):
        return 4

class Truck(VehicleWithEngine):
    def has_engine(self):
        return True
    def has_wheel(self):
        return 8

class Bicycle(Vehicle):
    def has_wheel(self):
        return 2  

# Creating objects and testing
Vehicleengine=[Car(),Truck()]
for vehicle in Vehicleengine:
    print("Does the vehicle have an engine?", vehicle.has_engine())
    print("Number of wheels:", vehicle.has_wheel())
    print()
noengine=[Bicycle()]
for v in noengine:
    print(" number of while in bicycle is ",v.has_wheel())