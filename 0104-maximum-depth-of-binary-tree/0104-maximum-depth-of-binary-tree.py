# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left) + 1
        r = self.maxDepth(root.right) + 1
        if l > r:
            return l
        return r

        