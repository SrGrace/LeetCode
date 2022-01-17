class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split(' ')
        
        if len(pattern) != len(st):
            return 0
        if len(set(pattern)) != len(set(st)):
            return 0
        
        hsh = dict()
        for i in range(len(pattern)):
            # if pattern[i] in hsh and hsh[pattern[i]] != st[i]:
            #     return 0
            # else:
            #     hsh[pattern[i]] = st[i]
            
            if pattern[i] not in hsh:
                hsh[pattern[i]] = st[i]
            else:
                if hsh[pattern[i]] != st[i]:
                    return 0
        
        return 1
        
    