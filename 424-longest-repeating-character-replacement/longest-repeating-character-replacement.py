class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if len(s) == 1:
            return 1

        left = 0
        longest = 0
        counts = {}
        max_freq = 0


        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] +=1
            else:
                counts[s[right]] = 1
            
            max_freq = max(max_freq, counts[s[right]])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left +=1

            longest = max(longest, right - left + 1)

        return longest