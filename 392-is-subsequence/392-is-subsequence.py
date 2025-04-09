class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        st = 0
        for i in range(len(s)):
            # print("before", st)
            st = t.find(s[i], st)
            # print("after", st)
            if st == -1:
                return False
            st += 1
        return True # O(n), O(1)
    
    
