class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0
        already_seen = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in already_seen:
                already_seen.remove(s[left])
                left += 1
            already_seen.add(s[right])
            longest = max(longest,right-left + 1)

        return longest
