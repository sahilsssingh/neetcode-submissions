# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        side = [None]

        def dfs(root, prev):
            if not root:
                if side[0] == "left":
                    prev.left = TreeNode(val)

                else:
                    prev.right = TreeNode(val)

                return
             
            if val < root.val:
                side[0] = "left"
                dfs(root.left, root)
            
            elif val > root.val:
                side[0] = "right"
                dfs(root.right, root)
        
        if not root:
            return TreeNode(val)

        dfs(root, root)
        return root