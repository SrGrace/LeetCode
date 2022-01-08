class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = [[[None]*n for _ in range(n)] for _ in range(n)]
        def dp(r1, c1, c2):
            r2 = r1+c1-c2  
            if (n == r1 or n == r2 or n == c1 or n == c2 
                    or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == n-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2]:
                return memo[r1][c1][c2]
            else:
                res = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                res += max(dp(r1, c1+1, c2+1), dp(r1+1, c1, c2+1),
                           dp(r1, c1+1, c2), dp(r1+1, c1, c2))
            memo[r1][c1][c2] = res
            return res
        
        # O(n^3), O(n^3)
        return max(0, dp(0, 0, 0))
    