# #randon module :
# import random
# ranNum = random.randint(1, 6)
# print(ranNum)
# ranList = ["sagar", "rakshas", "bissal", "amket", "harss", "chutta sand"]
# print(random.choice(ranList))
#
#
# #emoji module:
# import emoji
# print(emoji.demojize("😘"))
# print(emoji.emojize(":face_blowing_a_kiss:"))
# print("❤")
#
#
# #turtle graphics module
# import turtle
# turt1 = turtle.Turtle()
# turtle.delay(100)
# turt1.forward(300)
# turtle.delay(10)
# turt1.circle(69)
# turtle.done()
#
# #numPy module
# import numpy as np
# sampleArray1 = np.array([14, 25, 36, 47, 58, 69])
# print(sampleArray1)


# time module in python
import time
# for i in range(15):
#     print(i)
#     time.sleep(1)
print(time.gmtime(0))
currentTime = time.time()
print("the current time in seconds since epoch = ", currentTime)
print(time.ctime())
print(time.ctime(currentTime))
time.sleep(2)
print(time.ctime())
print(time.localtime())
print(time.asctime(time.localtime()))


