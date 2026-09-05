class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        copies = {}

        def dfs(node):
            if node in copies:
                return copies[node]

            new = Node(node.val)
            copies[node] = new

            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))

            return new

        return dfs(node)