# https://leetcode.com/problems/roman-to-integer/

class Solution(object):

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        final_Val = 0
        currentVal = ""
        previousVal = ""
        putVal = lambda x: (conversion_Dic[currentVal] - 2*conversion_Dic[previousVal])
        conversion_Dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(self.s)):
            currentVal = self.s[i]
            if i != 0:
                previousVal = self.s[i-1]
            if currentVal == "V" and previousVal == "I":
                final_Val += putVal(final_Val)

            elif currentVal == "X" and previousVal == "I":
                final_Val += putVal(final_Val)

            elif currentVal == "L" and previousVal == "X":
                final_Val += putVal(final_Val)

            elif currentVal == "C" and previousVal == "X":
                final_Val += putVal(final_Val)

            elif currentVal == "D" and previousVal == "C":
                final_Val += putVal(final_Val)

            elif currentVal == "M" and previousVal == "C":
                final_Val += putVal(final_Val)

            else:
                final_Val +=conversion_Dic[self.s[i]]
        return final_Val