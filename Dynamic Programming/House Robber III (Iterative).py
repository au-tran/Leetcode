# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def get_nodes_at_depth(root, dic, depth):
            if root is None:
                return 
            
            if depth not in nodes:
                nodes[depth] = []
            
            nodes[depth].append(root)
            
            get_nodes_at_depth(root.left, dic, depth+1)
            get_nodes_at_depth(root.right, dic, depth+1)
            
            return
        
        
        nodes = {}
        
        get_nodes_at_depth(root, nodes, 0)
        
        dp_with_root = {None: 0}
        dp_without_root = {None: 0}
        
        for depth in reversed(nodes):
            for node in nodes[depth]:
                dp_with_root[node] = node.val + dp_without_root.get(node.left, 0) + \
                dp_without_root.get(node.right, 0)
                
                dp_without_root[node] = max(dp_with_root.get(node.left, 0), \
                                           dp_without_root.get(node.left, 0)) + \
                max(dp_with_root.get(node.right, 0), dp_without_root.get(node.right, 0))
        
        
        return max(dp_without_root[root], dp_with_root[root])