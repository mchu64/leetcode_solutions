class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(char.lower() for char in s if char.isalnum())
        left = len(s)-1

        for x in range(len(s)-1):
            if s[x] != s[left]:
                return False
            left=left-1
        
        return True