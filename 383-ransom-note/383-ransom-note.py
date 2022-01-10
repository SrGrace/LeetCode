class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return 0
        
        cnt = collections.Counter(magazine)
        for idx, ch in enumerate(ransomNote):
            cnt[ch] -= 1
            if cnt[ch] < 0:
                return 0
        return 1