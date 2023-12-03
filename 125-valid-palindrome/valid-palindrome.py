class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i].lower()
        
        new_stringreverse = new_string[::-1]
        return True if new_stringreverse == new_string else False



        