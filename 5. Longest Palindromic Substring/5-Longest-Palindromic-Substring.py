class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
           odd = self.palindrom(s, i, i)
           print("odd - ", odd)
           even = self.palindrom(s, i, i+1)
           print("even - ", even)
           res = max(res, odd, even, key=len)
           print("int res - ", res)
        
        return res
    
    def palindrom(self, s, l, r):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
