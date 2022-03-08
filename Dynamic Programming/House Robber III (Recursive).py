# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def util(root):
            if root is None:
                return [0,0]

            left = util(root.left)
            right = util(root.right)

            withroot = root.val + left[1] + right[1]
            withoutroot = max(left) + max(right)

            return [withroot, withoutroot]
    
        return max(util(root))