class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return the truth of comparing the string to its reversed sequence
        return str(x) == str(x)[::-1]




test = Solution()

print(test.isPalindrome1(11))