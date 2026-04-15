# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            
            nxt = curr.next         # can be None
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        #<- 0 <- 1 -> 2 -> 3
        #        p
        #             c

        # iterate through the list once
        # at each node, node.next.prev = node, while node.next
        