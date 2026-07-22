class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # Outer Loop: This is the buy 
        for i in range(len(prices)):
            # Inner Loop: This is the sell 
            for j in range(i + 1, len(prices)):
                currentProfit = prices[j] - prices[i]

                if currentProfit > maxProfit:
                    maxProfit = currentProfit
        return maxProfit
    
