import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(-1)
        temp = dummy
        while heap:
            el = heapq.heappop(heap)
            temp.next = el[2]
            temp = temp.next

            if el[2].next:
                heapq.heappush(heap, (el[2].next.val ,el[1], el[2].next))
        
        return dummy.next