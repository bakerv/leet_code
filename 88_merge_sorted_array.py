class Solution:
    def merge_1(self, nums1, m: int, nums2: int, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index, entry in enumerate(nums2):
            nums1[m+index] = entry
        nums1.sort()

    def merge(self, nums1, m: int, nums2: int, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for index in range(m, m+n):
            nums1[index] = nums2[index - m]
        nums1.sort()