class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def dfs(root):
            if not root:
                return

            if root.val == key:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                # two children: find successor (smallest in right subtree)
                parent = root
                succ = root.right
                while succ.left:
                    parent = succ
                    succ = succ.left

                root.val = succ.val
                if parent.left == succ:
                    parent.left = succ.right
                else:
                    parent.right = succ.right

                return root

            if key < root.val:
                root.left = dfs(root.left)
            if key > root.val:
                root.right = dfs(root.right)

            return root

        return dfs(root)