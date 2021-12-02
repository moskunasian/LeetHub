# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # regular traversal of a BT
        # just keep an updated var for depth
        # when we reach end, just check for max currDepth
        
        self.maxDepth = 0
        def traverse(node, currDepth):
            if not node:
                if currDepth > self.maxDepth:
                    self.maxDepth = currDepth
                return
            traverse(node.left, currDepth+1)
            traverse(node.right, currDepth+1)
        traverse(root, 0)
        return self.maxDepth
        