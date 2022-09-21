def sampleFunc(*argument1, **argument2):
    for i in argument1:
        print(i)
    for j,k in argument2.items()
        print(f"this is {j}, {j} is a {k}")
sampleList = [22, "yo", "sagar", "rakshas"]
sampleDic = {"sagar":"khatri", "bissal":"vairagi", "rakshas":"sharma"}
sampleFunc(*sampleList, **sampleDic)