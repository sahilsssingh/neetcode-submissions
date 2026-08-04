# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        def reverse_k_nodes(head, k):
            prev = None
            curr = head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, curr  


        dummy = ListNode(-1)
        dummy.next = head
        group_prev = dummy  

        while has_k_nodes(group_prev.next, k):
            group_head = group_prev.next         
            new_head, next_group_start = reverse_k_nodes(group_head, k)

            group_prev.next = new_head              
            group_head.next = next_group_start        
            group_prev = group_head   
                           
        return dummy.next