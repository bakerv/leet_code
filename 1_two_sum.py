class Solution:
    def twoSum_brute_force(self, nums, target: int) -> int:
        for index_1, entry_1 in enumerate(nums):
            for index_2, entry_2 in enumerate(nums):
                if sum([entry_1,entry_2]) == target:
                    return [index_1, index_2]

    def twoSum(self, nums, target: int) -> int:
        previous_nums = dict()
        for index, entry in enumerate(nums):
            test = target - entry
            if test in previous_nums:
                return [previous_nums[test], index]
            previous_nums[entry] = index

test = Solution()

print(test.twoSum([2,7,11,15],9))