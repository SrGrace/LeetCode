class Solution {
public:
    bool isPalindrome(int x) {
        // string xx = to_string(x);
        // int l = 0, r = xx.length()-1;
        // while(l < r){
        //     if(xx[l++] != xx[r--]){
        //         return false;
        //     }
        // }
        // return true;
        
        if(x < 0 or (x%10 == 0 and x != 0))
            return false;
        
        int rev = 0;
        while(x > rev){
            rev = rev * 10 + x%10;
            x /= 10;
        }
        return rev == x or x == rev/10;
    }
};