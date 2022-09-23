# https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        conversionDic = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",90: "XC", 100: "C",               400: "CD", 500: "D", 900: "CM", 1000: "M" }
        inpInt = num
        finalAns = ""
        for keys, values in reversed(conversionDic.items()):
            if inpInt % keys != inpInt:
                finalAns += (inpInt // keys)*values
                inpInt = inpInt % keys
        return finalAns