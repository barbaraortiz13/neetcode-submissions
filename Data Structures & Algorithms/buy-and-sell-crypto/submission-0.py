class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []

        for p in range (len(prices)):
            for x in range(p+1, len(prices)):
                if prices[x]>= prices[p]:
                    profit = prices[x] - prices[p]
                    profits.append(profit)
        profits.append(0)
        
        hi = max(profits)

        return hi



        



        