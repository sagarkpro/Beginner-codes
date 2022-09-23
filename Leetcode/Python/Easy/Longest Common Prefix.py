# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            ans = ""
            minimumStr = min(strs, key = len)
            flag = 0
            for j in range(len(minimumStr)):
                for i in range(len(strs)-1):
                    if strs[i][j] == strs[i+1][j]:
                        flag = 1
                    else:
                        flag = 2
                        break
                if flag == 1:
                    ans += strs[i][j]
                elif flag  == 2:
                    break
            return ans