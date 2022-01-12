# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # create a head for a new linked list
        final_list_head = current_location = ListNode(0)

        # direct the pointer for the new list
        # only at nodes where head.val != val
        while head:
            if head.val == val:
                head = head.next
            else:
                current_location.next = head
                head = head.next
                current_location = current_location.next

        # detach unwanted trailing nodes from the new list
        current_location.next = None

        return final_list_head.next