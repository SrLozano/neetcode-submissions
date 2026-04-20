class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_buying_price = math.inf

        for i in range(0, len(prices)):
            if prices[i] < best_buying_price:
                best_buying_price = prices[i]
            selling_price = prices[i]
            max_profit = max(max_profit, selling_price - best_buying_price)

        return max_profit