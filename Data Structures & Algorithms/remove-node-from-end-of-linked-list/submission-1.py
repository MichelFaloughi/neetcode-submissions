# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #   1 -> 2 -> 3 -> 4 -> None            n = 2
        #   h
        #        s   
        #                  f

        #   5 -> None       n = 1
        #   h
        #   s
        #        f

        #   1 - > 2 -> None         n = 2
        #   h
        #   s
        #              f
        
        # init s and f n appart
        # slow -> head, 
        # fast -> slow
        # for _ in range(n): # TODO: check OBO
        #   fast = fast.next

        # if f is already None here, then the head has to go,
        #   return head.next

        # while f.next:
        #   increment both f and s

        # s.next = s.next.next
        # return head


        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head