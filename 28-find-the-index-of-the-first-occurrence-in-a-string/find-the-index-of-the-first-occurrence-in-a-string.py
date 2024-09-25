class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        needle_length = len(needle)
        haystack_length = len(haystack)

        left = 0

        for right in range(haystack_length-needle_length+1):
            if haystack[right:right+needle_length] == needle:
                return right
        
        return -1