def decoratorFunc(argFunc) :
    def interMediateFunc():
        print("you are in intermediate function")
        argFunc()
        print("arg function executed successfully")
    return interMediateFunc()
@decoratorFunc
def printFunc1():
    print("you are in function 1")


