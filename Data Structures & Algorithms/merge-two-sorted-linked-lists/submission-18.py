# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # init dummy = ListNode()
        # base case if both are none
        # recursive case will involve
        #   node.next = recursive call
        # return head which might be dummy.next ?
        # do i need the 'if both None' check ?

        dummy = ListNode()

        def helper(list1, list2):
            if not list1 and not list2:
                return None

            elif not list1:
                return list2
            elif not list2:
                return list1
            else:
                if list1.val < list2.val:
                    return ListNode(
                        val=list1.val,
                        next=helper(list1.next, list2)
                    )
                else:
                    return ListNode(
                        val=list2.val,
                        next=helper(list1, list2.next)
                    )
        
        dummy.next = helper(list1, list2)

        return dummy.next























        # dummy = ListNode()
        # curr = dummy

        # while list1 and list2:
        #     if list1.val > list2.val:
        #         curr.next = list2
        #         list2 = list2.next
        #     else:
        #         curr.next = list1
        #         list1 = list1.next
        #     curr = curr.next
        
        # if list1:
        #     curr.next = list1 
        # if list2:
        #     curr.next = list2

        # return dummy.next