class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        dict = {"}": "{", ")":"(","]":"["}

        for char in s:

            if char in dict.values():
                stack.append(char)
            elif stack and stack[-1] == dict[char]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False

        
                