def sqareList(x):
    return x*x
sampleList = [4,5,8,9,4,9,2,9]
squareList = list(map(sqareList, sampleList))    #here a lamba function can aslo be used (*1)
print(squareList)
sampleList2 = ["55", "99", "66", "77"]
print(list(map(int, sampleList2)))   #this will change the data in list from string to int

# (*1) :

print(list(map(lambda x:x*x, sampleList)))   #achieved the same task with lambda funtion in only 1 line