# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        res = ListNode(0)
        tmp = res
        while l1 and l2:
            val = l1.val + l2.val + add
            num = val % 10
            add = val // 10
            tmp.next = ListNode(num)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + add
            num = val % 10
            add = val // 10
            tmp.next = ListNode(num)
            tmp = tmp.next
            l1 = l1.next

        while l2:
            val = l2.val + add
            num = val % 10
            add = val // 10
            tmp.next = ListNode(num)
            tmp = tmp.next
            l2 = l2.next

        if add:
            tmp.next = ListNode(1)

        return res.next



