class A:
    classVar = "This is a variable in class A"
    def __init__(self):
        self.consVar = "this is a variable in class A's Constructor"

class B(A):
    classVar = "This is a variable overridden in class B"
    def __init__(self):
        # if the super function is defined before the overridden member then the member will be overridden normally.
        self.consVar = "This is a variable overridden in class B's Constructor"
        super().__init__()  #if super is defined after the overriden member then the override will override 😂 and the parent class's member will be executed.

instB = B()
print(instB.consVar)