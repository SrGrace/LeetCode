class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hsh = {}
        for ch in p:
            if ch in hsh:
                hsh[ch] += 1
            else:
                hsh[ch] = 1
        
        res = []
        len_p = len(p)
        # for i, ch in enumerate(s):
        #     if ch in p:
        #         tmp = s[i:i+len_p]
        #         # print(i, tmp)
        #         if char_map(tmp) == hsh_p:
        #             res.append(i)
        l, r = 0, 0
        while(r < len(s)):
            if s[r] in hsh:
                hsh[s[r]] -= 1
                if hsh[s[r]] >= 0:
                    len_p -= 1
            
            if len_p == 0:
                res.append(l)
            
            if r == l + len(p) - 1:
                if s[l] in hsh:
                    if hsh[s[l]] >= 0:
                        len_p += 1
                    hsh[s[l]] += 1
                l += 1
            r += 1
            
        return res
    