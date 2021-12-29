import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = collections.Counter(s)
        for index,entry in enumerate(s):
            if char_counts[entry] == 1:
                return index
        return -1

s = 'loveleetcode'
test = Solution()
print(test.firstUniqChar(s))