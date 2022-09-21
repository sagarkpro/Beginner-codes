# this is a dedicated code for time module
import time
initialTime = time.time()
print(initialTime)
x = 0
while x<1000:
    print("hello world")
    x+=1
print("time taken to complete while loop is : ", time.time()-initialTime, " seconds")
initialTimeFor = time.time()
for i in range(1000):
    print("hello world")
print("time taken to complete while loop is : ", time.time()-initialTimeFor, " seconds")
