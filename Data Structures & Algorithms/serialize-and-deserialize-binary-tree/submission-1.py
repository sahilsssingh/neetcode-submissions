# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if not node:
                res.append("n")

            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return 

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])

        i = 1
        while i < len(vals):
            node = q.popleft()

            if vals[i] != "n":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            if i < len(vals) and vals[i] != "n":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
            
        return root