# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x = str(x)
        temp1 = self.x[::-1]
        if temp1 == self.x :
            return True
        else :
            return False