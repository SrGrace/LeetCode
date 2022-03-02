class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # O(n), O(n)
        # dp = [0]*n
        # dp[0], dp[1] = 1, 2
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        #
        # return dp[-1]
        
        # O(n), O(1)
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a+b
            a = tmp
        return b
    
    