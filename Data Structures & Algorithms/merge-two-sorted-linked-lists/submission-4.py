# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        temp = list1
        prev = None
        while list2:
            if (temp is not None) and (temp.val <= list2.val):
                prev = temp
                temp = temp.next
            else:
                if prev is None:
                    list1 = list2
                    temp2 = list2.next
                    list1.next = temp
                    list2 = temp2
                    prev = list1

                else:
                    prev.next = list2
                    temp2 = list2.next
                    list2.next = temp
                    list2 = temp2
                    prev = prev.next
                
        return list1