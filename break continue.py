while (True):
    xyz =0
    print("enter a no. greater than 100")
    xyz = int(input())
    if xyz > 100:
        print("congratulations, you entered a number greater than 100")
        break
    else:
        print("try again")
        continue