class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for x in range(len(nums)):
            if target-nums[x] in hashmap:
                return [x,hashmap[target-nums[x]]]
            hashmap[nums[x]] = x

        return null
            