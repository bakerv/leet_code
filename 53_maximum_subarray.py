import math

class Solution:
    def maxSubArray_brute_force(self, nums) -> int:
        current_best = -math.inf
        # iterate through every starting position
        for sub_array in range(len(nums)):
            test_max = 0
            # find the maximum possible sum from each starting position
            for entry in nums[sub_array:len(nums)]:
                test_max += entry
                current_best = max(current_best, test_max)

        return current_best

    # Kadane's Algorithm
    def maxSubArray(self, nums) -> int:
        current_max = 0
        overall_max = -math.inf
        for entry in nums:
            # determines best starting point for the sub array
            # and sums values beginning at that point
            current_max = max(entry, current_max + entry)
            # determines the sum at the optimal end point for the sub array
            overall_max = max(overall_max, current_max)
        return overall_max

test = [-1,7,4,-17,12]
solution = Solution()
print(solution.maxSubArray(test))