# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow = ListNode(-1, next=head)
        fast = head
        for i in range(n):
            if fast:
                fast = fast.next
            else:
                raise
        while fast:
            fast = fast.next
            slow = slow.next
        tmp_next = slow.next.next
        slow.next = tmp_next
        if slow.val == -1:
            return slow.next
        else:
            return head