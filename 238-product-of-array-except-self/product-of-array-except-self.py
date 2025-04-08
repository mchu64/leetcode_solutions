class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # First pass: calculate total product and count zeros
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        # Second pass: calculate the result based on the zero count
        result = []
        
        if zero_count > 1:
            # If there are more than one zero, all results will be zero
            return [0] * len(nums)

        for num in nums:
            if zero_count == 1:
                # If there's exactly one zero, the result is non-zero only where the zero was
                if num == 0:
                    result.append(total_product)  # product of all non-zero elements
                else:
                    result.append(0)  # other positions get zero
            else:
                # No zeros, normal division
                result.append(total_product // num)
        
        return result

