# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # None <- 0 <- 1  
        
        # None <- 2 <- 3  None
        #              h

        # base case
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next) 
        head.next.next = head
        head.next = None


        return new_head
        

        

        # want to have ⬇️
        # None <- 0 <- 1 <- 2 <- 3
        #                        h