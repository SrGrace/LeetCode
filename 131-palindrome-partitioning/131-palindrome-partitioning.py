class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # def isPalindrom(s):
        #     return s[:] == s[::-1]
        
        # res = [[x for x in s]]
        # for k in range(1, len(s)):
        #     tmp = list()
        #     for i in range(0, len(s), k):
        #         print(s[:i], s[i:])
        #         if isPalindrom(s[:i]) and s[:i] != '':
        #             tmp.append(s[:i])
        #         if isPalindrom(s[i:]) and s[i:] != '':
        #             tmp.append(s[i:])
        #     res.append(tmp)
        # print(res)
        # return res
        
        def bactracking(st, ed, tmp):
            if st == ed:
                res.append(tmp[:]) 
            
            for i in range(st, ed):
                cur = s[st:i+1]
                if cur[:] == cur[::-1]:  # isPalindrom
                    tmp.append(cur)
                    bactracking(i+1, ed, tmp)
                    tmp.pop()
        res = []
        bactracking(0, len(s), [])
        return res