class Solution:
    def containsDuplicate(self, nums) -> bool:
        return not len(nums) == len(set(nums))

solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))
