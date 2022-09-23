// https://leetcode.com/problems/palindrome-number/

class Solution {
public:
    bool isPalindrome(int x) {
        string xS = to_string(x);
        int j = xS.length(), k = ((int)j/2)-1, ans;
        
        for(int i = 0; i <=k; i++)
        {
            if(xS[i] == xS[j-1])
            {
                ans = 1;
                j--;
            }
                
            else
            {
                ans = 0;
                break;
            }
  
        }
        if(ans == 1)
            return true;
        else 
            return false;
    }
};