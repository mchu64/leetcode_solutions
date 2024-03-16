class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        import heapq

        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        while(k > 1):
            -heapq.heappop(max_heap)
            k= k- 1

        x = -max_heap[0]
        return x