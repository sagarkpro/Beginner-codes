#NOTE : The exceptions file should have a blank line at the end for the program to run properly


import os
def prettyFolder(path:str, exceptions, ftype:str) :
    os.chdir(path)
    with open(exceptions, "r") as file:
        i = 1
        temp = file.readlines()
        a = []
        j = 1
        for i in temp:
            a.append(i[0:-1])
        for items in os.listdir():
            fname = str(items[-4:])
            if items in a:
                pass
            elif fname == ftype:
                temp2 = f"{j}{ftype}"
                os.rename(items, temp2)
                j += 1
            elif os.path.isfile(items) and items != exceptions:
                os.rename(items, f"{items.capitalize()}")

prettyFolder(input("Enter the path you want to prettify"), input("Enter the name of exception txt file w/ .txt"), input("Enter the file type you want to rename w/ '.' e.g .txt"))
