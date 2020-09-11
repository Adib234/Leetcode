class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        maxprofit = 0
        tempmin = float('inf')

        for i in range(len(prices)):
            if tempmin > prices[i]:
                tempmin = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i]-tempmin)
        return maxprofit
