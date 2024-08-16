class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = list("qwertyuiopQWERTYUIOP")
        second = list("asdfghjklASDFGHJKL")
        third = list("zxcvbnmZXCVBNM")
        output = []
        for x in words:
            if all(char in first for char in x):
                output.append(x)
            elif all(char in second for char in x):
                output.append(x)
            elif all(char in third for char in x):
                output.append(x)
        return output
        