class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hsh = dict()
        res, last_match = 0, -1
        for i, ch in enumerate(s):
            if ch in hsh and last_match < hsh[ch]:
                last_match = hsh[ch]
            res = max(res, i - last_match)
            hsh[ch] = i
        return res # O(n), O(n)
        
        
