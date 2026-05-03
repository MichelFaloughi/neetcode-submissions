# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l, r = head, head

        for _ in range(n):
            r = r.next
        
        if not r: # if r is None, l didn't move
            return head.next

        while r.next:
            l, r = l.next, r.next

        l.next = l.next.next # TODO: check garbage collection worked

        return head # TODO: maybe add a checker
        
        # [ 1, 2, None ], n = 2 
        #   l
        #         r


        # [ 1, 2, 3, 4 ], n = 2
        #      p  l  r



        # [ 1, 2, 3, 4, 5, 6, 7 ], n = 7
        #   l                 r
        #         

        # [ 1, 2, 3, 4, 5, 7 ]

        # init l, r to head
        # increment r n times
        # increment both while r.next is not null
        # rewire

        # add a checker to see if l never moved (stayed on head) then head = head.next 
        # add a chceker if n = 1 ?
        
        # TODO: consider when you remove the head itself
        #
        