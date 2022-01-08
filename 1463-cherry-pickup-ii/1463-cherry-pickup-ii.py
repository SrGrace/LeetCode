class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dp(r, c1, c2):
            if c1 < 0 or c1 >= n or c2 < 0 or c2 >= n:
                return float('-inf')
            
            res = 0
            res += grid[r][c1] + (c1 != c2) * grid[r][c2]
            
            if r != m-1: # not last row
                res += max(dp(r+1, new_c1, new_c2) 
                           for new_c1 in [c1, c1+1, c1-1]
                           for new_c2 in [c2, c2+1, c2-1])
            
            return res
        
        # O(m(n)^2), O(m(n)^2)
        return dp(0, 0, n-1)
            
        