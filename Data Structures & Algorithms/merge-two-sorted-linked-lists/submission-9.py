# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode() # save for return
        temp = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else: # list1.val >= list2.val
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next

        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2

        return dummy_node.next

    #    1   2   4
    #    1   3   5
    # t
    # d

    # d
    #   d-1-1-2-3-4
            
# learnings:
# Why dummy node ? It avoids special-casing the first node. Without it, you'd need separate logic to figure out which node becomes the head before starting the loop. The dummy node lets you just append everything uniformly, then return dummy.next.

