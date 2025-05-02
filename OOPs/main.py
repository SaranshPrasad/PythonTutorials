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
l.greet()
l.sound()
l.display_name()

# Multiple Inheritance

class Friend:
    def friend(self):
        print(f"{self.name} is a friendly dog.")

class Golden(Lab, Friend):
    def color(self):
        print(f"{self.name} is of golden color.")

gold = Golden("Tobby")
gold.display_name()
gold.friend()
gold.greet()
gold.sound()
