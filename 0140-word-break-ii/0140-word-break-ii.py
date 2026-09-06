class Solution:
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            ans = []

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word in words:
                    rest = dfs(j)

                    for x in rest:
                        if x == "":
                            ans.append(word)
                        else:
                            ans.append(word + " " + x)

            memo[i] = ans
            return ans

        return dfs(0)