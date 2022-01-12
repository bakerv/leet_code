# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed_list = None
        while head:
            # get the current value of the head
            current_value = head

            # advance the head to the next value to avoid overwriting
            head = head.next

            # point the current value to the list of previously seen values
            current_value.next = reversed_list

            # update the list of previously seen values
            reversed_list = current_value

        return reversed_list

    # solution taken from the discussion section of leetcode from user tusizi