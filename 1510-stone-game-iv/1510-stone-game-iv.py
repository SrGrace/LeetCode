class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(remains):
            if not remains:
                return False
            
            sqrt = int(remains**0.5)
            for i in range(1, sqrt+1):
                if not dfs(remains - i*i):
                    return True
            return False
        
        return dfs(n)
    
    