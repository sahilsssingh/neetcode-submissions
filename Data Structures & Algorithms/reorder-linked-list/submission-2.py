# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        end = slow
        slow = slow.next
        end.next = None

        prev = None
        while slow:
            forward = slow.next
            slow.next = prev
            prev = slow
            slow = forward
        
        temp = head
        while temp and prev:
            front1 = temp.next
            front2 = prev.next
            temp.next = prev
            prev.next = front1
            temp = front1
            prev = front2