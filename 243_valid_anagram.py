import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_letters = collections.Counter(s)
        t_letters = collections.Counter(t)

        return s_letters == t_letters
