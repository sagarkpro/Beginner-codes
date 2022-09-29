birthDate = str(input("Enter your bithdate in this format - 14th Nov 1980 or 1st Nov 1980 or 3rd Dec 1980"))
birthList = birthDate.split(" ")
monthDic = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Oct":9, "Nov":10, "Sep":11, "Dec":12}
convertBirth = int(f"{birthList[0][0:-2]}{monthDic[birthList[1]]}{birthList[2]}")
print("Your Birth Date in Decimal Number is : ", convertBirth)
print("Your Your Birth Date in Binary number is : ", format(convertBirth, 'b'))