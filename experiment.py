class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        numsNew = []
        for i in range(len(nums)):
            if val != nums[i]:
                numsNew.append(nums[i])
        nums = numsNew