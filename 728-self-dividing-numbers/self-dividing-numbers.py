class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        ans = []

        for x in range(left,right+1):
            string = str(x)
            flag = True
            if '0' in string:
                continue

            for z in string:
                    if x % int(z) != 0:
                        flag = False
            if flag == True:
                ans.append(x)

        return ans