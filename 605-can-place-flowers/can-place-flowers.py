class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        counter = 0

        while i < len(flowerbed):
            if i == 0 and len(flowerbed)>1:
                after = i+1
                if flowerbed[0] == 0 and flowerbed[after] == 0:
                    flowerbed[0] = 1
                    i+=1
                    counter+=1
            if i > 0 and i < len(flowerbed)-1:
                last = i-1
                current = i
                after = i+1
                if flowerbed[last] == 0 and flowerbed[current] == 0 and flowerbed[after] == 0:
                    counter += 1 
                    flowerbed[current] = 1
                    i+=1

            if i == len(flowerbed)-1:
                if flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    counter+=1
            i+=1


        if counter >= n:
            return True
        return False