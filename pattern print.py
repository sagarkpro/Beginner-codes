patternInp = input("What letter do you want to print?")
amountPattern = int(input("How mant times do you want to print the pattern?"))
orderInp = int(input("to print in decending order enter 1 and 2 for vice versa"))
if orderInp == 1:
    for i in range(amountPattern):
        print(i*patternInp)
else:
    while amountPattern>0:
        print(amountPattern*patternInp)
        amountPattern -=1
print("program completed")
