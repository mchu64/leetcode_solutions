class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        mem = set()
        left = 0
        longest = 0
        

        for right in range(len(s)):
            while s[right] in mem:
                mem.remove(s[left])
                left +=1
            mem.add(s[right])
            longest = max(longest,right-left +1)

        return longest