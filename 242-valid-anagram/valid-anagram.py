class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        
        for x in range(len(s)):
            if s[x] != t[x]:
                return False

        return True