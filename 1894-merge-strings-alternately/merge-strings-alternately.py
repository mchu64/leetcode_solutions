class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


        answer = []
        length1 = len(word1)
        length2 = len(word2)
        counter = 0

        while counter < length1 and counter < length2:
            answer.append(word1[counter])
            answer.append(word2[counter])
            counter += 1
        
        if counter < length1:
            answer.append(word1[counter:])

        if counter < length2:
            answer.append(word2[counter:])
        
        return "".join(answer)

        
            

