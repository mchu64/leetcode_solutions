class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_element = prices[0]

        for price in prices:
            if price < min_element:
                min_element = price
            elif price - min_element > max_profit:
                max_profit = price - min_element

        return max_profit