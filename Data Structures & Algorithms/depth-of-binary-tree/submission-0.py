# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, currMax):
            if not node:
                return currMax

            return max(dfs(node.left, currMax+1), dfs(node.right, currMax+1))
        
        return dfs(root, 0)


        # return something
        # know when to increment
        # compare to max_depth
        