
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict = {}

        for x in nums:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        sorted_nums = sorted(dict.keys(), key=lambda x: dict[x], reverse=True)
        answer = []
        for x in range(k):
            answer.append(sorted_nums[x])
        return answer