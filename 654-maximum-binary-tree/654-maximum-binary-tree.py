# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(vals):
            
            # getting max for curr node and idx
            root = TreeNode(max(vals))
            idx = vals.index(max(vals))
            
            # prefix portion for left subtree
            prefix = vals[:idx]
            if prefix:
                root.left = recurse(prefix)
            
            # suffix portion for right subtree
            suffix = vals[idx+1:]
            if suffix:
                root.right = recurse(suffix)
            
            return root
        
        return recurse(nums)
        