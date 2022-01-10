import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        note_count = collections.Counter(magazine)
        for char in ransomNote:
            # exit if the character is not in the magazine
            if char not in note_count:
                return False

            # update availability for each character
            note_count[char] += -1
            if note_count[char] < 0:
                return False

        return True

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        required = collections.Counter(ransomNote)
        available = collections.Counter(magazine)
        for count in required:
            if available[count] - required[count] < 0:
                return False
        return True

ransom_note='aa'
magazine='ab'
test = Solution()
print(test.canConstruct(ransom_note, magazine))
