def greet(name):
    print("Hello", name)
greet("Abi")
def add(a,b):
    return a+b
result = add(5,3)
print(result)
#function with default paramater
def greet(name="Guest"):
    print("Hello",name)
    greet()

#functions and without return value
def numbers(a, b):
    print(a, b)

numbers(20, 10)
#another example
def order_bill(item, price):
    print("item:", item)
    print("price:", price)

order_bill("pizza", 200)

#functions and with return value
def total_bill(price, tax):
    return price + tax
bill = total_bill(1000, 50)
print(bill)

def greet(name):
    print("hello",name)
greet("mano")

#keyword arguments
def student(name, age):
    print(name, age)
student(age=20, name="Abi")

#another example
def marks(name, marks):
    print(name, marks)
marks(name="kaviya", marks=100)

#*args(tuple)
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function("Emil", "Tobias", "Linus")
#another example
def numbers(*args):
    print(args)
numbers(1,2,3,4)

#kwargs**(dictionary)
def student(**data):
    print(data)
student(name="Kaviya", mark=100, city="Chennai")

#lamda 
add = lambda a, b: a + b
print(add(2,3))
#another example
mul = lambda a,b: a*b
print(mul(3,4))

#local scope
def myfunc():
  x = 300
  print(x)
myfunc()
#another example
def numbers():
    a=100
    print(a)
numbers()

#global scope
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
#recursion
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
count(3)
#A Fibonacci Sequence is a series of numbers where each number is created by adding the previous two numbers
#formula Fn​=Fn−1​+Fn−2​
n = 10
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c