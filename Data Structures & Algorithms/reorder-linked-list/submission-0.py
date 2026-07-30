# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        lastel = slow
        slow = slow.next
        lastel.next = None

        prev = None
        while slow:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front

        temp = head
        while temp and prev:
            front1 = temp.next
            temp.next = prev
            front2 = prev.next
            prev.next = front1
            temp = front1
            prev = front2