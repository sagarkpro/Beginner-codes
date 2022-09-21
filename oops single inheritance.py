class ToyotaCars:
    def __init__(self, carName, horsePower, numCylinders):
        self.carName = carName
        self.horsePower = horsePower
        self.numCylinders = numCylinders
    def prinCartInfo(self):
        return f"The name of the car is {self.carName} and it has {self.horsePower} and {self.numCylinders} Cylinders"


furtuner = ToyotaCars("Toyota Fortuner", 201.15, 4)
innova = ToyotaCars("Toyota Innova Crysta", 148, 4)
hilux = ToyotaCars("Toyota Hilux", 201.15, 4)
print(furtuner.prinCartInfo())
print(innova.prinCartInfo())

#Single Inheritance e.g :

class CarType(ToyotaCars):
    def __init__(self, carType):
        self.carType = carType

    def printCarType(self):
        return f"The type of car is {self.carType}"


innova = CarType("MPV")
print(innova.printCarType())