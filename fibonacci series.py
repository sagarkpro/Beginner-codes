# fiboSeries = [0, 1]
# seriesLen = int(input("Enter the length of the series"))
# rangeVar = 2
# currentNum = 0
# upparPos = 0
# lowerPos = 0
# if seriesLen == 1:
#     print(fiboSeries[0])
# elif seriesLen == 2:
#     print(fiboSeries[0:])
# else:
#     while rangeVar < seriesLen:
#         lowerPos = rangeVar-2
#         upparPos = rangeVar-1
#         currentNum = (fiboSeries[lowerPos]+fiboSeries[upparPos])
#         print(currentNum)
#         fiboSeries.append(currentNum)
#         rangeVar += 1
#     print(fiboSeries)
# nthTerm = int(input("which term of fibo series do you want to print?"))
# print(fiboSeries[nthTerm])
seriesLen = int(input("Enter the length of the series"))
def fiboNum(a):
    if a == 0:
        return 0
    elif a==1:
        return 1
    else:
        return fiboNum(a-2) + fiboNum(a-1)
print(fiboNum(seriesLen-1))
fiboSeries = []
tempNum = 0
for tempNum in range(seriesLen):
    fiboSeries.append(fiboNum(tempNum))
print(fiboSeries)

