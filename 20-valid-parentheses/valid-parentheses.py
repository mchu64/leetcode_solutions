class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        
        stack = []

        closed = {")": "(", "}":"{","]":"["}

        for x in s:
            if x in closed.values():
                stack.append(x)
            elif stack and closed[x] == stack[-1]:
                stack.pop()
            else:
                return False


        if len(stack) == 0:
            return True
            
