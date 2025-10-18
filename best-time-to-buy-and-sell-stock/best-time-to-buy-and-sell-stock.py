class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfitAfterKTrans(prices, k):
            buy = [float(inf)]*(k+1)
            sell = [0]*(k+1)
            for p in prices:
                for k in range(1, k+1):
                    buy[k] = min(buy[k], p-sell[k-1])
                    sell[k] = max(sell[k], p-buy[k])
            return sell[-1]
        
        return maxProfitAfterKTrans(prices, 1) # O(k*n), O(k)



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n), O(1)
        min_price, max_profit = float(inf), 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p-min_price)
    
        return max_profit
