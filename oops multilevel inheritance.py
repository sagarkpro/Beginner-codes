class ComputerScience:
    coding = 1
    def printComputerScience(self):
        print(f"can do coding {self.coding} times")

class ElectronicsComms(ComputerScience):
    autocad = 1
    def printElectronicsComms(self):
        print(f"{self.printComputerScience()} and can do autocad {self.autocad} times")

class ElectricalElectronics(ElectronicsComms):
    powergen = 1
    def printElectricalElectronics(self):
        print(f"{self.printElectronicsComms()} and can generate power {self.powergen}")

gupta = ComputerScience()
aashishSir = ElectronicsComms()
sagar = ElectricalElectronics()


sagar.printElectricalElectronics()  #will print none because there is no return provided in the print funtions.

#class ElectricalElectronics has everything that class ElectronicsComms has as well as class ComputerScience has
#class ElectronicsComms has everything that class ComputerScience has but it doesn't have anything that class ElectricalElectronics has
#class ComputerScience has nothing but only its own functions and variables.