from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def moveforward(self):
        pass
    @abstractmethod
    def backward(self):
        pass
    @abstractmethod
    def fm(self):
        pass

class swift(Car):
    def moveforward(self):
        print("swift is moving forward")
    def backward(self):
        print("swift is moving backward")
    def fm(self):
        print("swift is playing fm")

swift=swift()
swift.backward()

#another example
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d = Dog()
d.sound()
        


    