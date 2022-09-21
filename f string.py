# f strings are useful for fast coding and code readability
nameInp = input("Hello, What is your name?")
occupationInp = input("What is your occupation?")
str1 = f"my name is {nameInp}, I am a {occupationInp}"
print(str1)
str2 = f"this is another sample string {34+35}, {255/5}, {str1}"
print(str2)