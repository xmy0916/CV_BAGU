# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k_flag = []
        for l in lists:
            if not l:
                k_flag.append(0)
            else:
                k_flag.append(1)
        new_head = ListNode(-1)
        res = new_head
        length = len(lists)
        while sum(k_flag) >= 1:
            min_index = -1
            min_value = float("inf")
            for i in range(length):
                if k_flag[i] == 0:
                    continue
                if lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            tmp_next = new_head.next
            new_head.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            new_head.next.next = tmp_next
            new_head = new_head.next
            if not lists[min_index]:
                k_flag[min_index] = 0
        return res.next