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



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n), O(1)
        initial_buy_price, max_profit = prices[0], 0
        for current_price in prices[1:]:
            if initial_buy_price > current_price:
                initial_buy_price = current_price
            max_profit = max(max_profit, current_price - initial_buy_price)

        return max_profit
