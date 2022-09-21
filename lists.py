members = ["sagar", "jaytant", "blah blah", 4]
print(members)
print(members[3])
nums = [1, 6, 3, 8, 0, 2]
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
print(nums[:2])
print(members[-2:])
print(nums[::-1])
print(nums[::2])
nums.append(34)
print(nums)
nums.insert(0,88)
print(nums)
nums.remove(2)
print(nums)
print(max(nums))
print(min(nums))
nums.pop()
print(nums)
#mutable - changebale
#immutable - cant't change
#tuple :
tp = (1, 2, 3, 4, 5) #cant't change
print(tp)
a = 34
b = 35
a, b =b, a
print(a, b)