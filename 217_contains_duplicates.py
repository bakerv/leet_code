class Solution:
    def containsDuplicate(self, nums) -> bool:
        return not len(nums) == len(set(nums))

pizza = Solution()

print(pizza.containsDuplicate([1,2,3,1]))
