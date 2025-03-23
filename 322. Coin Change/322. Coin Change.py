class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

        # O(len(coins)*amount) = O(n*m), O(m)

        """
        example: coins = [1, 2, 5] and amount = 11

        # dp initialize
        dp = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

        for coin in coins: [1, 2, 5]
            for x in range(coin, amount+1) [1, 12), [2, 12), [5, 12)

        for coin = 1
            For each i from 1 to 11, update dp[i] = min(dp[i], dp[i - 1] + 1).
            dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        for coin = 2
            For each i from 2 to 11, update dp[i] = min(dp[i], dp[2 - 1] + 1).
            dp = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

        for coin = 5
            For each i from 5 to 11, update dp[i] = min(dp[i], dp[5 - 1] + 1).   
            dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]

        dp[11] = 3 [1, 5, 5]
        """
