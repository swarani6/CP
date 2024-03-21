class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprofit=0
        minpurchase=prices[0]
        for i in range(1,len(prices)):
            maxprofit=max(maxprofit,prices[i]-minpurchase)
            minpurchase=min(minpurchase,prices[i])
        return maxprofit
