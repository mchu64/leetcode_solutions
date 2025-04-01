class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        best = 0

        count = {}

        l = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] +=1
            else:
                count[s[r]] = 1

            
            while((r - l + 1) - max(count.values()) > k):
                count[s[l]] -=1
                l+=1

            best = max(best, r - l +1)

        return best