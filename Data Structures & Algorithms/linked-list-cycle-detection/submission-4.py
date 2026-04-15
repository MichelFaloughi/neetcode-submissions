# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()
        
        while head:
            len1 = len(seen)
            seen.add(head)
            len2 = len(seen)

            if len1 == len2:
                return True
            
            head = head.next
        
        return False













# learnings:
# - it's always the tail tha cycles back
# - are all the vals of the nodes unique ?