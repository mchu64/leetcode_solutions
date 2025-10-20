class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []

        for x in nums:
            heapq.heappush(heap, x)

        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)


        