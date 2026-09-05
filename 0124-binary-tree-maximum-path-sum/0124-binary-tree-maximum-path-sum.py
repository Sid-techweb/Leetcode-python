class Solution:
    def maxPathSum(self, root):
        ans = float("-inf")

        def dfs(node):
            nonlocal ans

            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            ans = max(ans, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return ans