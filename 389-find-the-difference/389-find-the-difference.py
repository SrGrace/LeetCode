class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hsh = collections.Counter(s)
        for ch in t:
            if ch in hsh and hsh[ch] > 0:
                hsh[ch] -= 1
            else:
                return ch # O(n), O(n)
        
