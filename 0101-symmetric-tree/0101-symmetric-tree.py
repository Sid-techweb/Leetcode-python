class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True 
            if not n1 or not n2:
                return False
            if n1 and n2 and n1.val==n2.val:
                return is_mirror(n1.left,n2.right) and is_mirror(n1.right,n2.left)
            return False
        return is_mirror(root.left,root.right)
            