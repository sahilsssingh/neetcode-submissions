# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        t1, t2, i = l1, l2, 1
        sum1 = sum2 = 0
        while t1 and t2:
            sum1 += t1.val * i
            sum2 += t2.val * i
            i *= 10
            t1 = t1.next
            t2 = t2.next

        while t1:
            sum1 += t1.val * i
            i *= 10
            t1 = t1.next

        while t2:
            sum2 += t2.val * i
            i *= 10
            t2 = t2.next

        total = sum1 + sum2
        if total == 0:
            return ListNode(0)

        dummy = ListNode(-1)
        ans = dummy
        while total > 0:
            ans.next = ListNode(total % 10)
            total = total // 10
            ans = ans.next

        return dummy.next