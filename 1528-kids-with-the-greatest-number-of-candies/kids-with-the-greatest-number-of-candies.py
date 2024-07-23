class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        

        output = []

        for x in range(len(candies)):
            candies[x] += extraCandies
            if max(candies) == candies[x]:
                output.append(True)
            else:
                output.append(False)
            candies[x] -= extraCandies
        return output