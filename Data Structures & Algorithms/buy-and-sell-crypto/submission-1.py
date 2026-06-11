class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - least
            if profit > max_profit:
                max_profit = profit
            if prices[i] < least:
                least = prices[i]
        
        return max_profit