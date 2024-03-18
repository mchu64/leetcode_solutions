class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        left = 0
        s = list(s)
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            else:
                if s[left] not in vowels:
                    left += 1
                if s[right] not in vowels:
                    right -= 1

        return ''.join(s)
