# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
        #  0 -> 1 -> 2 -> 3 -> None

        if not head or not head.next:
            return head

        # fetching the head
        new_head = self.reverseList(head.next)

        # switching pointers around
        head.next.next = head
        head.next = None

        return new_head


        






        #  None <- 0 <- 1 <- 2 <- 3