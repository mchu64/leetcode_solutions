class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        setnums = set(nums)

        longest = 0

        for num in setnums:
            if num - 1 not in setnums:
                current = num
                current_streak = 1

                while current + 1 in setnums:
                    current += 1
                    current_streak +=1

                if current_streak > longest:
                    longest = current_streak

        return longest

