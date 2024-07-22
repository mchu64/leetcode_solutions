class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        array = [0] + flowerbed + [0]
        for x in range(1,len(array)-1):
            if array[x] == 0 and array[x-1] == 0 and array[x+1] == 0:
                array[x] =1
                n-=1
                
        if n <= 0:
            return True