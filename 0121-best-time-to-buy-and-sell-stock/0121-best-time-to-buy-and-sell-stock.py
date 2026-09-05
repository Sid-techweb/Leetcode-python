class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                ans = max(ans, prices[i] - buy)

        return ans