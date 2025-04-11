class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfitAfterKTrans(prices, K):
            buy = [float(inf)]*(K+1)
            sell = [0]*(K+1)
            for p in prices:
                for k in range(1, K+1):
                    buy[k] = min(buy[k], p-sell[k-1])
                    sell[k] = max(sell[k], p-buy[k])
            return sell[-1]
        
        return maxProfitAfterKTrans(prices, k) # O(k*n), O(k)
