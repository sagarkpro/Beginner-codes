// https://leetcode.com/problems/roman-to-integer/

class Solution {
public:
    int converter(char x){
        int y;
        switch(x){
            case 'I':
                y = 1;
                break;
            case 'V':
                y = 5;
                break;
            case 'X':
                y = 10;
                break;
            case 'L':
                y = 50;
                break;
            case 'C':
                y = 100;
                break;
            case 'D':
                y = 500;
                break;
            case 'M':
                y = 1000;
                break;
        }
        return y;
    }
    int romanToInt(string s) {
        int n = s.length(), finalans = 0;
        for(int i = 0; i<n; i++){
            char ss = s[i];
            finalans += converter(ss);
            if(i-1 >= 0){
                char s1 = s[i-1];
                if(s[i-1] == 'I' && s[i] == 'V')
                    finalans -= 2*(converter(s1));
                else if(s[i-1] == 'I' && s[i] == 'X')

                    finalans -= 2*(converter(s1));
                
                else if(s[i-1] == 'X' && s[i] == 'L')
                    finalans -= 2*(converter(s1));
                else if(s[i-1] == 'X' && s[i] == 'C')
                    finalans -= 2*(converter(s1));
                
                else if(s[i-1] == 'C' && s[i] == 'D')
                    finalans -= 2*(converter(s1));
                else if(s[i-1] == 'C' && s[i] == 'M')
                    finalans -= 2*(converter(s1));
                
                }
        
            }
        return finalans;
        }
};