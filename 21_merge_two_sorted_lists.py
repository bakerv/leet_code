# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return sorted(list(sum([list1, list2], [])))

list1 = [1,2,4,7, 5]

list2 = [1,3,4]
test = Solution()
print(test.mergeTwoLists(list1, list2))