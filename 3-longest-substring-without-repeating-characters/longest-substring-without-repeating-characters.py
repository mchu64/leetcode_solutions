class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        left = 0
        hashmap = {}
        for right in range(len(s)):
            if s[right] in hashmap and hashmap[s[right]] >= left:
                left = hashmap[s[right]] + 1
            hashmap[s[right]] = right
            longest = max(longest, right-left + 1)
        return longest
            