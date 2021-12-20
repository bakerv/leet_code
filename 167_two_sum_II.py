class Solution:
    def twoSum(self, numbers, target: int) -> int:
        previous_nums = dict()
        for index, entry in enumerate(numbers):
            test = target - entry
            if test in previous_nums:
                return [previous_nums[test], index + 1]
            previous_nums[entry] = index + 1