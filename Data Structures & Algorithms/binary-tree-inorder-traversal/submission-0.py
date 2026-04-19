# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []

        def is_leaf(node):
            return node is not None and (node.left is None) and (node.right is None)

        def dfs(node):

            if is_leaf(node):
                res.append(node.val)
                return
            
            if node:
                if node.left:
                    dfs(node.left)
                res.append(node.val)
                
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return res

