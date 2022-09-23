// https://leetcode.com/problems/longest-common-prefix/

#include<string>
using namespace std;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 1)
        {
            return strs[0];
        }
        else
        {
            string ans = "";
            int minPos, flag = 0;
            for(int i=0; i<=strs.size()-1;i++)
            {
                if(strs[i]<strs[i+1])
                    minPos = i;
            }
            int s = strs[minPos].size()-1;
            for(int i = 0; i<=s; i++)
            {
                for(int j=0; j<=strs.size();j++)
                {
                    if(strs[i][j] == strs[i+1][j])
                    {
                        flag = 1;
                        continue;
                    }
                    else
                    {
                        flag = 0;
                        break;
                    }
                    if(flag == 1)
                        ans += strs[i][j];
                    else if(flag == 0)
                        break;
                }
            }
            return ans;
            
        }
    }
};