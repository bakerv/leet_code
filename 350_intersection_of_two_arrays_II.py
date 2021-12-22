class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        results = []
        if len(nums1) < len(nums2):
            for item in nums1:
                if item in nums2:
                    results.append(item)
                    nums2.remove(item)
        else:
            for item in nums2:
                if item in nums1:
                    results.append(item)
                    nums1.remove(item)
        return results