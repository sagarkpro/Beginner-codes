# https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i != j :
                    return [i,j]
