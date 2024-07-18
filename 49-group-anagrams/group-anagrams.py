class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        output = {}

        for x in strs:
            key = "".join(sorted(x))
            if key not in output:
                output[key] = []
                output[key].append(x)
            else:
                output[key].append(x)
        return output.values() 