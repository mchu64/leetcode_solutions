class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []
        nums.sort()

        for x in range(len(nums)-1):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            current=nums[x]
            left = x+1
            right = len(nums)-1
            while left < right:
                total = current + nums[left] + nums[right]
                if total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    answer.append([current,nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                    
        
        return answer

