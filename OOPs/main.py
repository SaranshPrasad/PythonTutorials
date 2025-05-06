# Class :-  A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.


# __init__ method: Initializes the name and age attributes when a new object is created.
# self :-  parameter is a reference to the current instance of the class. It allows us to access the attributes and methods of the object.
class Dog:
    species = "Labrador" # Class Attribute
    def __init__(self,name,age): # Constructor 
        self.name = name # Instance Attribute
        self.age  = age  # Instance Attribute

d = Dog("Boldy",5) # Object of class dog
# print(d.name,d.age,d.species)

# Inheritence 

# Single Level Inheritence
class Doggy:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f'{self.name} is my name.')

class Boldy(Doggy):
    def sound(self):
        print(f'{self.name} barks')

b = Boldy("Boldy")
# b.display_name()
# b.sound()

# Multillevel Inheritance 
class Lab(Boldy):
    def greet(self):
        print(f"{self.name} says Welcome Malik")

l = Lab("Max")
# l.greet()
# l.sound()
# l.display_name()

# Multiple Inheritance

class Friend:
    def friend(self):
        print(f"{self.name} is a friendly dog.")

class Golden(Lab, Friend):
    def color(self):
        print(f"{self.name} is of golden color.")

gold = Golden("Tobby")
# gold.display_name()
# gold.friend()
# gold.greet()
# gold.sound()


# Polymorphism

# Overriding
class Doberman(Doggy):
    def display_name(self):
        print(f"{self.name} is active") # overriding parent class function.

dob = Doberman("Doodo")
# dob.display_name()

class Calculator:
    def add(self, *args): # Method Overloading 
        sum = 0
        for a in args:
            sum += a
        return sum


cal = Calculator()
# print(cal.add(1,2,2,3,4,5,6,7,8,10))
# print(cal.add(1,2))
        

# Encapsulation
# Public Members: Easily accessible, such as name.
# Protected Members: Used with a single _, such as _breed. Access is discouraged but allowed in subclasses.
# Private Members: Used with __, such as __age. Access requires getter and setter methods.

class Car:
    def __init__(self,model,age,company):
        self.company = company
        self._model = model # protected attribute, to make protected use _
        self.__age = age # private attribute , to make private use __
     
    def get_company(self):
        print(self.company)
    
    # Getter & Setter to set the private attribute __age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid")

car = Car(911,1,"Porche")
# car.set_age(2)
# car.get_company()
# print(car.get_age())
# car.set_age(220)


# Data Abstraction

# Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on “what to do” rather than “how to do it.”

# Types of Abstraction:
# 1. Partial Abstraction: Abstract class contains both abstract and concrete methods.
# 2. Full Abstraction: Abstract class contains only abstract methods (like interfaces).
from abc import ABC, abstractmethod
class Human:
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Insaan(Human): # partial abstraction
    def sound(self):
        print("Hehehehehehe!")

saru = Insaan("Saru")
saru.sound()
print(saru.name)