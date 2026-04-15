# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # assuming tiebreak goes to list1
        # 1 -> 2 -> 4 -> None
        #      l1
        #
        # 1 -> 3 -> 5 -> None
        #      l2
        #
        # h -> 1 -> 1
        #           c

        # h = dummy
        # curr = h

        # while both lists
        # compare values, choose max, tie it to h, increment corresponding list and curr
        # 
        # if list1, append it and return h.next
        # if list2, append it and return h.next
        # return h.next

        h = ListNode() # dummy node
        curr = h

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        # at least one of the two lists are done
        if list1:
            curr.next = list1
            return h.next # because h is dummy remember
        if list2:
            curr.next = list2
            return h.next
        
        return h.next




