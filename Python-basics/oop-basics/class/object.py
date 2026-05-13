#simple
class Car:
    brand = "BMW"
c1 = Car()
print(c1.brand)

#another example
class car:
    no_of_wheels=0
    mileage=0.0
    no_0f_airbags=0
    def moveforward():
        print("car is moving")
    def backward():
        print("car is moving backward")
car1= car()
print(car1.no_0f_airbags)
print(car1.no_of_wheels)
print(car1.mileage)

#constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#another example
class flower:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
f1 = flower("rose","red")
print(f1.name)
print(f1.colour)

#constructor and destructor
class Student:
    # constructor
    def __init__(self, name):
        self.name = name
        print("Object created")
    # string method
    def __str__(self):
        return "Student name is " + self.name
    # destructor
    def __del__(self):
        print("Object deleted")
s1 = Student("Subika")
print(s1)
        