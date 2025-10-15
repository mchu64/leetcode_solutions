class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        output = {}

        for word in strs:
            if "".join(sorted(word)) in output:
                output["".join(sorted(word))].append(word)
            else:
                output["".join(sorted(word))] = [word]
        return output.values()