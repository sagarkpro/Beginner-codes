# water = 28 min (17 glasses of 200ml = 3.4 L  water)
# eyes = 30 min
# movement = 45 min
import time
import pygame
pygame.mixer.init()
def stopMusic():
    print("To stop the music playback type 'Yes'")
    if input() == "yes" or "Yes" or "YES":
        pygame.mixer.music.stop()
def writeLog(a):
    msgOpDic = {1:f"{time.asctime()} : Drank a glass of water \n", 2:f"{time.asctime()} : Relaxed the eyes \n",
                3:f"{time.asctime()} : Did some exercise \n"}
    with open("temp.txt", "w") as fileLogging:
        fileLogging.write(msgOpDic[a])
    with open("Health concious Programmer.txt", "r") as fileLogging:
        with open("temp.txt", "a") as tempLogging:
            tempLogging.write(fileLogging.read())
    with open("Health concious Programmer.txt", "w") as fileLogging:
        with open("temp.txt", "r") as tempLogging:
            fileLogging.write(tempLogging.read())
currentTime = time.localtime()
officeTimeStart = (9, 0, 0)
officeTimeEnd = (17, 0, 0)
outputList = {"eye" : "Please Relax and Exercise your eyes by looking at something 20meters away from you",
              "water" : "It's time to drink a glass of water", "exercise" : "Go do some exercise"}
while currentTime[3:5] > officeTimeStart and  currentTime[3:5] < officeTimeEnd :
    print("You in Office, Health Conscious Programmer is running \n")
    print("Current Time is : ", time.asctime(), "\n")
    timeElapsed = (int(currentTime[3]) * 60 + currentTime[4]) - 540
    if timeElapsed%28==0 :
        print(timeElapsed)
        print(outputList["water"])
        pygame.mixer.music.load("water.mp3")
        pygame.mixer.music.play(-1,0,1000)
        stopMusic()
        writeLog(1)
    if timeElapsed%30==0 :
        print(timeElapsed)
        print(outputList["eye"])
        pygame.mixer.music.load("eye.mp3")
        pygame.mixer.music.play(-1, 0, 1000)
        stopMusic()
        writeLog(2)
    if timeElapsed%45==0 :
        print(timeElapsed)
        print (outputList["exercise"])
        pygame.mixer.music.load("exersice.mp3")
        pygame.mixer.music.play(-1, 0, 1000)
        stopMusic()
        writeLog(3)
    time.sleep(60)
print("You are not in office, the program ends \n")
print("Current Time is : ", time.asctime())
exit(0)