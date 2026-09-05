class Solution:
    def connect(self, root):
        if root is None:
            return root

        q = [root]

        while q:
            n = len(q)

            for i in range(n):
                node = q.pop(0)

                if i < n - 1:
                    node.next = q[0]

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root