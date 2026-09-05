class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        x = ""

        for c in s:
            if c.isalnum():
                x += c

        return x == x[::-1]