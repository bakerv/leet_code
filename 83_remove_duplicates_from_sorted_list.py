# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # new linked list to return
        final_list_head = current_location = ListNode(0)

        # intitial comparison value
        current_val = None
        while head:
            # point the new list to unique values
            if head.val != current_val:
                current_val = head.val
                current_location.next = head
                head = head.next
                current_location = current_location.next

            # cycle to the next element when the value is not unique
            else:
                head = head.next

        # remove inapprpriate pointers from the end of the list
        current_location.next = None

        return final_list_head.next