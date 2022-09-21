sampleList = ["sagar", "bissal", "rakshas", "xyz", "abc"]
for indx, itm in enumerate(sampleList): #enumerate will give the index of the list as well as the item.
    if indx%2 == 0:
        print(f"my name is {sampleList[indx]}")
