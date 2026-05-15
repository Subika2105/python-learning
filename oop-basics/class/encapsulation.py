#data hiding
class Bank:
    def __init__(self):
        self.__balance = 5000
    def display(self):
        print(self.__balance)
b1 = Bank()
b1.display()

#getter/setter
class marks:
    def __init__(self):
        pass
    def __set__(self, instance, value):
        pass
    def __get__(self, instance, owner):
        pass

class Marks:
    def __init__(self):
        self.value = 1
    def __set__(self, instance, value):
        self.value = value
    def __get__(self, instance, owner):
        return self.value
class Student:
    marks = Marks()
s = Student()
s.marks = 95
print(s.marks)