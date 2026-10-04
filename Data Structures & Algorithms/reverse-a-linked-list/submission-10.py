# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  None 0 -> 1 -> 2 -> 3 -> None 
        #  p    c 

        p, c = None, head
        while c:
            t = c.next
            c.next = p
            p, c = c, t
        return p
        #     None <- 0  1 -> 2 -> 3 -> None 
        #             p       t
        #                c