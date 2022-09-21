dis = {"sagar":"khatri", "vishal":"bairagi", "harsh":"bhatewara", "gotm":{"chutiya":"maha chutiya", "rogi" : "prem rogi", "baal" : "laude ka baal"} }
print(dis)
print(dis["sagar"])
print(dis["gotm"]["baal"]) #dictionary within dictionary
dis["aniket"] = "panchal" #adding items
dis.update({"ajay":"rathod"}) #this method is better than above method for some reasons
print(dis)
del dis["aniket"] #delete
print(dis)
# dis2 = dis #this doesn't create new dictionary, it just points to dis
dis2 = dis.copy() #this creates a new copy of dis i.e. dis2
print(dis.items())
print(list(dis.keys())[1])
