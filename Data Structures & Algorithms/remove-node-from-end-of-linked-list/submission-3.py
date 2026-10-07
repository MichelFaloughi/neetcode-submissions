# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #   1 -> 2 -> 3 -> 4 -> None        n = 2
        #   h
        #        s
        #                  f

        #   5 -> None               n = 1
        #   h
        #        f
        #   s
        
        # init slow, fast to head
        # space them by n

        # keep incrementing both until fast.next is None
        # you know slow is at the node you want to delete

        slow, fast = head, head
        
        # space slow & fast by n
        for _ in range(n):
            fast = fast.next

        if not fast:
            return slow.next # or head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next 

        return head
