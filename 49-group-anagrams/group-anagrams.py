class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        

        output = {}

        for x in strs:
            if "".join(sorted(x)) not in output.keys():
                output["".join(sorted(x))] = []
                output["".join(sorted(x))].append(x)
            else:
                output["".join(sorted(x))].append(x)
        return output.values() 