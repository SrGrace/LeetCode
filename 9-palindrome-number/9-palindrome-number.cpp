class Solution {
public:
    bool isPalindrome(int x) {
        string xx = to_string(x);
        int l = 0, r = xx.length()-1;
        while(l < r){
            if(xx[l++] != xx[r--]){
                return false;
            }
        }
        return true;
        
    }
};