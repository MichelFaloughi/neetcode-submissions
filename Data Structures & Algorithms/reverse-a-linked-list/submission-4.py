# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        

        
        # p, c = None, h
        #   0 -> 1 -> 2 -> 3 ->
        # p c
        # 
        # temp = c.next
        # c.next = p
        #   <- 0 -> 1 -> 2 -> 3 ->
        # p    c    t
        # p = c
        #   <- 0 -> 1 -> 2 -> 3 ->
        #      c    t
        #      p
        # c = t
        #   <- 0 -> 1 -> 2 -> 3 ->
        #           t
        #      p    c
