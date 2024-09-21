class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        max = 0

        for x in range(len(prices)):
            if lowest > prices[x]:
                lowest = prices[x]
            if prices[x] - lowest > max:
                max = prices[x] - lowest


        return max
