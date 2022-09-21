# to create private and protected members of class you need to specify an underscore before the name of that name.
# 1 underscore = protected member
# 2 underscore = private member
# NOTE : to access the private member you need to access it in a unique way that is _classname__membername, this is called "Name Mangling"
#Note2 : in python the public private protected doesn't really mean anything because you can still modify and access the private members outside the class. It is only a indication
# for the programmer that it should not be modified outside the class.

# Here's a example code

class ExampleCode:
    member1 = "This is a public member"
    _member2 = "This is a Protected member"
    __member3 = "This is a private member"
class Example2(ExampleCode):
    pass  #you need to do this to make an empty class

objEg = ExampleCode()
print(objEg.member1)
print(objEg._member2)
print(objEg._ExampleCode__member3)

obj2 = Example2()
print(obj2.member1)
print(obj2._member2)
print(obj2._ExampleCode__member3)