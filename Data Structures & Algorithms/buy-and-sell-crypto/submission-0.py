class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(2, len(prices)):
            
            selling_price = prices[i]
            buying_price = min(prices[:i-1])

            max_profit = max(max_profit, selling_price - buying_price)

        return max_profit