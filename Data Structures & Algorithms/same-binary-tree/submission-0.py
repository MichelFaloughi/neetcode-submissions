# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # traverse the both trees, keep comparing nodes until one pair doesn't match
        def traversal_checker(p, q):
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return ( traversal_checker(p.left, q.left) and 
                        traversal_checker(p.right, q.right) )
            else:
                return False
                
        return traversal_checker(p, q)
            

        