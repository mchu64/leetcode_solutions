class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        p = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                temp = prices[right] - prices[left]
                p = max(p,temp)
            else:
                left = right
            right+=1

        return p
