class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buying_price = math.inf

        for i in range(0, len(prices)):
            best_buying_price = min(prices[i], best_buying_price)
            max_profit = max(max_profit, prices[i] - best_buying_price)

        return max_profit