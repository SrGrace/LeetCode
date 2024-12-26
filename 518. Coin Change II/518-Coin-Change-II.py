class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1): # to avoid duplicate counting
                dp[i] += dp[i-coin]
        print(dp)
        return dp[-1]
