#syntax
print("hello world")
#text
print("barbie")
print("sk")
#numbers
print(12)
print(25)

#python variables
x = 5
y = "Hello, World!"
print(x)
print(y)

#variables names(store values(_))
student_name = "Subika"
print(student_name)

#python statements
print("hello world")
print("have a good day")

#example
x=5
y="john"
print(type(x))
print(type(y))

#data types
car = {
    "brand": "BMW",
    "price": 500000
}
print(car)
print(type(car))
print(car["brand"])#accessing dictionary values
#float
a=10.4
b=20.5
print(a+b)
print(type(a+b))
#set
a={1,2,3}
print(a)
print(type(a))

#python numbers
x=100
y=23.5
z=2+5j
print(type(x))
print(type(y))
print(type(z))

#python casting
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#example
x = 1
a = float(x)
b = str(x)
print(a)
print(b)

#strings
a="python programming"
print(a[1:2])
print(a.capitalize)
print(a.upper)
print(a.lower)
print(a.replace("y","n"))
print(a.split("y"))
print(a.startswith("p"))
print(a.endswith("g"))
#fprmat string
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#operators(arithmetic)
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

#comparison operator
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#memembership operator
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("orange" not in fruits)

#fronzen sets(once created cannot be changed)
colors = frozenset(["red", "blue", "green"])
for i in colors:
     print(colors)

#if condition
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

#while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#for
fruits=["apple","banana","pineapple"]
for i in fruits:
    print(i)
    if fruits=="banana":
        break

#range(start,stop)
for i in range(1, 6):
    print(i)

for i in range(1,2,1):
    print(i)

#arrays
cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
cars[1] = "Toyota"
print(cars)

#function
def my_function():
  print("Hello from a function")
my_function()
#arguments
def add(a, b):
    print(a + b)
add(10, 20)
#positional arguments
def student(name, age):
    print(name)
    print(age)
student("Subika", 21)
#keyword arguments
def student(name, age):
    print(name)
    print(age)
student(age=21, name="Subika")
#args
def fruits(*args):
    print(args)
fruits("apple","banana")

#another example
def numbers(*args):
    for i in args:
        print(i)
numbers(10, 20, 30)

#arbitary keyword arguments
def student(**kwargs):
    print(kwargs)
student(name="Subika", age=21,city="chennai")

#lambda function
add = lambda a, b: a + b
print(add(10, 20))

#recursion
def numbers(n):
    if n == 0:
        return
    print(n)
    numbers(n - 1)
numbers(5)

#fibonacci  sequence(next number=previous two numbers sum)
a = 0
b = 1
for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c

#class/objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello, my name is", self.name)
p1 = Person("John", 36)
p1.greet()

#another example
class dog:
    def __init__(self,name,age):
        self.name = name
        self.name = age
    def bark(self):
        print(self.name,"says woof")
d1 = dog("tiger",1)
d1.bark()

