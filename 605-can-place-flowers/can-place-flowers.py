class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while i < len(flowerbed):
            if i == 0 and len(flowerbed)>1:
                if flowerbed[0] == 0 and flowerbed[i+1] == 0:
                    flowerbed[0] = 1
                    i+=1
                    n-=1
            if i > 0 and i < len(flowerbed)-1: 
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n-=1
                    flowerbed[i] = 1
                    i+=1
            if i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n-=1
            i+=1
        if n <= 0:
            return True