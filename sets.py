# set can store only unique items
l = [1, 2, 3, 4]
print(l)
print(type(l))
s = set([1, 2, 3, 4, 5, 6])
print(s)
print(type(s))
s2 = set()
s2.add(1)
s2.add(2)
s2.add(2) # 2 will be added only one time
print(s2)
s2.remove(1)
print(s2)