# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #    1 -> 2 -> 3 -> 2
        #         |         |
        #          --------- 
        #         ^

        # seen = {1, 2, 3, 4 }


        # 1 -> 2 -> 2 -> 3 -> 4 -> 3 -> None
        # ^

        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False




        