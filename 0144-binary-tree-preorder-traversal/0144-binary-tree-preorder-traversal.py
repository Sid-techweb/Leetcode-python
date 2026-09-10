class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        
        st = [root]

        while st:
            node = st.pop()
            res.append(node.val)

            if node.right:
                st.append(node.right)
            
            if node.left:
                st.append(node.left)
        
        return res