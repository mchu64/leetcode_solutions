
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = {}
        answer = []

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)

        for x in range(k):
            answer.append(sorted_counter[x][0])
        
        return answer