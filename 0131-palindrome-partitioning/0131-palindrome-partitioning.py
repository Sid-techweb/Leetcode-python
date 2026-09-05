class Solution:
    def partition(self, s):
        ans = []

        def backtrack(i, path):
            if i == len(s):
                ans.append(path[:])
                return

            for j in range(i, len(s)):
                x = s[i:j + 1]

                if x == x[::-1]:
                    path.append(x)
                    backtrack(j + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans