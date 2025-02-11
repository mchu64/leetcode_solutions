class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and s[l].isalnum() == False:
                l += 1
            while l < r and s[r].isalnum() == False:
                r -= 1

            
            if s[l].lower() != s[r].lower():
                return False

            l +=1
            r -=1



        return True
