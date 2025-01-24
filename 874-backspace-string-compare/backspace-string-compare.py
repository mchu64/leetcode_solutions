class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        Sstack = []
        Tstack = []
        for x in s:
            if x != "#":
                Sstack.append(x)
            if Sstack and x == "#":
                Sstack.pop()

        for x in t:
            if x != "#":
                Tstack.append(x)
            if Tstack and x == "#":
                Tstack.pop()
        
        return Sstack == Tstack