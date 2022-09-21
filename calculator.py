def addexp(a, b):
    print(a+b)
def subexp(a, b):
    print(a-b)
def mulexp(a,b):
    print(a*b)
def divexp(a,b):
    print(a/b)


userExp = input("Enter your expression, (only 2 number with a arithmatic sign in between them without space)")
op1 = 1
op2 = 1
for i in range(len(userExp)):
    if userExp[i] == "+":
        op1 = float(userExp[:i])
        op2 = float(userExp[i+1:])
        addexp(op1,op2)
    elif userExp[i] == "-":
        op1 = float(userExp[:i])
        op2 = float(userExp[i+1:])
        subexp(op1,op2)
    elif userExp[i] == "*":
        op1 = float(userExp[:i])
        op2 = float(userExp[i+1:])
        mulexp(op1,op2)
    elif userExp[i] == "/":
        op1 = float(userExp[:i])
        op2 = float(userExp[i+1:])
        divexp(op1,op2)
