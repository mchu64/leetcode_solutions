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
            
            profit = price - min_element
        
            if profit > max_profit:
                max_profit = profit

        return max_profit