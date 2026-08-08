# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            if not root:
                return -1

            if (not root.left and not root.right):
                return 0

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            self.diameter = max(self.diameter, left + right)

            return max(left, right)

        dfs(root)
        return self.diameter