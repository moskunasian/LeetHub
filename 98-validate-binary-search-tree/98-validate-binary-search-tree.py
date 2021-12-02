# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # inorder traversal of a valid BST will result in sorted list
        # after traversal check if list is sorted and that will give answer
        
        self.shouldBeSorted = []
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            self.shouldBeSorted.append(node.val)
            traverse(node.right)
        traverse(root)
        
        for i in range(1, len(self.shouldBeSorted)):
            if self.shouldBeSorted[i] <= self.shouldBeSorted[i - 1]:
                return False
        return True
        