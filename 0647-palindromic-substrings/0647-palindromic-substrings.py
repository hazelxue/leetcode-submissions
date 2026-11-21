class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j]: whether s[i:j] is palidromic
        # dp[i + 1][j - 1]
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        count += 1
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna