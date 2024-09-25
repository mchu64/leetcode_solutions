class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)-1
        counter = 0

        while length >= 0 and s[length] == " ":
            length-=1

        while length >= 0 and s[length] != " ":
            length-=1
            counter+=1

        return counter