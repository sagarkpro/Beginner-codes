// https://leetcode.com/problems/integer-to-roman/

class Solution {
public:
    string conDic[13] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
    string finalAns  = "";
    int conInt[13] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
    string intToRoman(int num) 
    {
        for(int i = 12; i >= 0; i--)
        {
            int s = num%conInt[i];
            if (s != num)
            {
                int p = int(num/conInt[i]);
                for(int j = 0; j<p; j++)
                    finalAns += conDic[i];
                num = s;
            }
        }
        return finalAns;
        
    }
};