class ToyotaCars:
    def __init__(self, XcarName, XhorsePower, XnumCylinders):
        self.carName = XcarName
        self.horsePower = XhorsePower
        self.numCylinders = XnumCylinders
    def prinCartInfo(self):
        return f"The name of the car is {self.carName} and it has {self.horsePower} and {self.numCylinders} Cylinders"


furtuner = ToyotaCars("Toyota Fortuner", 201.15, 4)
innova = ToyotaCars("Toyota Innova Crysta", 148, 4)
hilux = ToyotaCars("Toyota Hilux", 201.15, 4)
print(furtuner.prinCartInfo())
print(innova.prinCartInfo())