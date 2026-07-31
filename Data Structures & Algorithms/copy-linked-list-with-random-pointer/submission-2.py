"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        temp = head
        while temp:
            forward = temp.next
            temp.next = Node(temp.val)
            temp.next.next = forward
            temp = temp.next.next

        temp = head
        while temp:
            temp.next.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        dummy = Node(-1)
        temp = head
        ans = dummy
        while temp:
            ans.next = temp.next
            temp.next = temp.next.next
            temp = temp.next
            ans = ans.next
        
        return dummy.next