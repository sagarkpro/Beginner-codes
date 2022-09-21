class ToyotaCars:
    carName = "abcd efgh"
    def __init__(self, carName, horsePower, numCylinders):  #this is a constructor
        self.carName = carName
        self.horsePower = horsePower
        self.numCylinders = numCylinders
    def printCartInfo(self):
        return f"The name of the car is {self.carName} and it has {self.horsePower} Horse Power and {self.numCylinders} Cylinders"


    @classmethod
    def chngClassVars(cls, var):     #This can change the class variables itself which is not possible by other means
        cls.carName = var

    @classmethod
    def acceptValues(cls, stringVal):  #This func will accept the vales from a single string and then split it to make a list, It is also a alternate to init constructor
        values = stringVal.split("-")
        return cls(values[0], values[1], values[2])


    # the same accept value funtion can also work by using args function :

    @classmethod
    def betterAcceptValues(cls, stringVal):
        return cls(*stringVal.split("-"))

    # Static Method : it can be used to define a normal funtion that has nothing to do with the class but it will run only in that class.

    @staticmethod
    def normalFunc(anyVar):
        return f"This is what you have entered : {anyVar}"
ToyotaCars.chngClassVars("Fortuner")
print(ToyotaCars.carName)

innova = ToyotaCars.acceptValues("Toyota Innova Crysta-148-4")
print(innova.printCartInfo())

hilux = ToyotaCars.betterAcceptValues("Toyota Hilux-201.15-4")
print(hilux.printCartInfo())

print(ToyotaCars.normalFunc("YO yo yo 1 to 3 to 6 to the 9, representing the ABQ, what up Biaatch??"))


