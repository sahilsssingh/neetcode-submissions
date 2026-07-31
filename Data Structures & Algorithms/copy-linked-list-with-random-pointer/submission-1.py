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
        hash_dict = {}
        while temp:
            hash_dict[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            hash_dict[temp].next = hash_dict[temp.next] if temp.next else None
            hash_dict[temp].random = hash_dict[temp.random] if temp.random else None
            temp = temp.next

        return hash_dict[head]