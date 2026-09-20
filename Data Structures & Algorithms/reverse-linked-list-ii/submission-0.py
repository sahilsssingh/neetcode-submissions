# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, head)

        #find starting
        temp = dummy
        count = 0

        while count < left - 1:
            temp = temp.next
            count += 1
        
        before_left = temp
        temp = temp.next
        count += 1

        left_start = temp

        #reverse the part
        prev = None
        while count <= right:
            front = temp.next
            temp.next = prev
            count += 1
            prev = temp
            temp = front
        
        #rewiring
        left_start.next = temp
        before_left.next = prev

        return dummy.next