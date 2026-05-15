class vehicle:
    no_of_wheels=2
    def moveforward(self):
        print("vehicle is moving forward")
class car(vehicle):#inheritance(parent class/child class)
    no_of_airbags=3
car1=car()
print("car is moving forward")
print(car1.no_of_airbags)