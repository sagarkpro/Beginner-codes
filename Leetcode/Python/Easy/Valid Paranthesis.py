# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        conditions = {"(": ")", "{": "}", "[": "]"}
        temp = []
        sList = list(s)
        for i in sList:
            if i in conditions:
                temp.append(i)
            elif len(temp) > 0 and conditions[temp[len(temp) - 1]] == i:
                temp.pop()
            else:
                return False
        if len(temp) == 0:
            return True