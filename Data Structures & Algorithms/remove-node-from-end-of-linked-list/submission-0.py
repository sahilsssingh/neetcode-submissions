# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        node = length - n

        dummy = ListNode(-1)
        dummy.next = head
        count = 0
        current = dummy
        while count < node:
            current = current.next
            count += 1
        
        prev = current
        current = current.next
        prev.next = current.next
        return dummy.next