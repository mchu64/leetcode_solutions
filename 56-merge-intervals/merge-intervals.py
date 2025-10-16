class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals = sorted(intervals)
        res = []
        
        for x in intervals:
            if not res or res[-1][1] < x[0]:
                res.append(x)
            else:
                res[-1][1] = max(res[-1][1], x[1])
        
        return res
