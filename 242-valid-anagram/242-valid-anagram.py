class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return 0
        cnt = collections.Counter(s)
        for idx, ch in enumerate(t):
            cnt[ch] -= 1
            if cnt[ch] < 0:
                return 0
        return 1 # O(n), O(n)
