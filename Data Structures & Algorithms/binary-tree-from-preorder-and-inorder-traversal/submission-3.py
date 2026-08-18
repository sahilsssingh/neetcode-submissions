# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        
        hash_dict = {}
        for i, val in enumerate(inorder):
            hash_dict[val] = i
        
        def helper(p_start, p_end, i_start, i_end):

            if p_start > p_end:
                return None
            
            root = TreeNode(preorder[p_start])
            mid = hash_dict[root.val]
            left_size = mid - i_start
            
            root.left = helper(p_start + 1, p_start + left_size, i_start, mid - 1)
            root.right = helper(p_start + left_size + 1, p_end, mid + 1, i_end)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)