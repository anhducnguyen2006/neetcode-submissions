class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        ret = 0
        for i in range(1, len(prices)): 
            ret = max(ret, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])
    
        return ret