class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()  # Sort the input list

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return output
