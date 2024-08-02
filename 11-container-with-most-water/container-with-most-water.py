class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        dict = {}

        left = 0
        right = len(height)-1
        counter = 0

        shorter = 0

        while left < right:
            width = right-left
            if height[left] < height[right]:
                shorter = height[left]
            else:
                shorter = height[right]
            dict[counter] = width*shorter
            counter+=1
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
                
        return max(dict.values())
        