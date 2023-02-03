# listExp = [11,2,4,34,4,5,6,4,4]
# val = 4
# for i in range(len(listExp)):
#     if val == listExp[i]:
#         print(listExp[i])
nums = [1,22,3,44,5,8,6,6,4,5,6,6,7,6,8,6,9,6,9,6]
val = 6
numsNew = []

for i in range(len(nums)):
    if val != nums[i]:
        numsNew.append(nums[i])
print(numsNew)

