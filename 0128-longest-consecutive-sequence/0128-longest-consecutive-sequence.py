class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0

        for x in s:
            if x - 1 not in s:
                count = 1

                while x + count in s:
                    count += 1

                ans = max(ans, count)

        return ans