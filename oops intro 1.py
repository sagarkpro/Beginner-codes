class ToyotaCars:
    carName = str()
    horsePower = float()
    numCylinders = int()
    def printDetails(self):
        return f"The car Toyota {self.carName} Has {self.horsePower} Horse Power and {self.numCylinders} Cylinders"


fortuner = ToyotaCars()
fortuner.carName = "Fortuner"
fortuner.numCylinders = 4
fortuner.horsePower = 201.15

innova = ToyotaCars()
innova.carName = "Innova Crysta"
innova.horsePower = 148
innova.numCylinders = 4

hilux = ToyotaCars()
hilux.carName = "Hilux"
hilux.horsePower = 201.15
hilux.numCylinders = 4

print(fortuner.printDetails())
print(innova.printDetails())
print(hilux.printDetails())
print(fortuner.carName)