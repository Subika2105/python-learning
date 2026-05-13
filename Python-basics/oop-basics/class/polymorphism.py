#same method but different behavior
class Car:
    def move(self):
        print("Car is running")
class Plane:
    def move(self):
        print("Plane is flying")
c = Car()
p = Plane()
c.move()
p.move()

#compile time polymorphism
class Math:
    def add(self, a, b, c=0):
        print(a + b + c)
m = Math()
m.add(2, 3)
m.add(2, 3, 4)
#another example
class Math:
    def add(self, *numbers):
        print(sum(numbers))
m = Math()
m.add(1, 2)
m.add(1, 2, 3)
m.add(1, 2, 3, 4, 5)

#method overriding
class father:
    def say_hello(self):
        print("hello from father")
class child(father):
    def say_hello(self):
        print("hello from child")
child=child()
child.say_hello()
