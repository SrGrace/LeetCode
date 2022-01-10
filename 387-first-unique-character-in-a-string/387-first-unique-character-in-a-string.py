class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        print(cnt)
        for i, ch in enumerate(s):
            if cnt[ch] == 1:
                return i
        return -1
                