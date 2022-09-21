# wrong ans = 45*58, 59/7, 27*38, 89/69
print("Enter operator")
ope = input()
print("enter first no.")
fn = int(input())
print("enter secod no.")
sn = int(input())
if ope=="+":
    print(fn + sn)
elif ope=="-":
    print(fn-sn)
elif ope=="*":
    if fn==45 and sn==58 or sn==45 and fn==58:
        print("2615")
    elif ope == "*" and fn == 27 and sn == 38 or sn == 27 and fn == 38:
        print("1024")
    else:
        print(fn*sn)
elif ope=="/":
    if ope == "/" and fn == 59 and sn == 7:
        print("9.42")
    elif ope == "/" and fn == 89 and sn == 69:
        print("1.48")
    else:
        print(fn/sn)
