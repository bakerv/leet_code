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
        # create a head for a new linked list
        final_list_head = current_location = ListNode(0)

        # add the location of the smaller value as the next element of the new list
        # and advance the list that contained the smaller value
        # as well as the new list
        while list1 and list2:
            if list1.val < list2.val:
                current_location.next = list1
                list1 = list1.next
            else:
                current_location.next = list2
                list2 = list2.next
            current_location = current_location.next

        # after exhausting the shorter list
        # aim the pointer at the remaining sorted list
        current_location.next = list1 or list2

        # return only elements from list1 and list2
        # not the head from the new list
        return final_list_head.next