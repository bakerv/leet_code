class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        arabic_value = 0
        for index, character in enumerate(s):
            try:
                if translation[character] < translation[s[index+1]]:
                    arabic_value += -translation[character]
                else:
                    arabic_value += translation[character]
            except:
                arabic_value += translation[character]

        return arabic_value

test = Solution()
M = 'MIX'

print(test.romanToInt(M))



