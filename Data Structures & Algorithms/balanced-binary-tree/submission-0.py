# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) -> list[bool, int]:
            if not node:            # if leaf
                return [True, 0]    # balanced, height

            l = dfs(node.left)      # [bool, int]
            r = dfs(node.right)

            balanced = (l[0] and r[0] and 
                        abs(l[1] - r[1]) <= 1)
            height = max(l[1], r[1]) + 1 # TODO: check if with +1? 

            return [balanced, height]
        
        return dfs(root)[0]