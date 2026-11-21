class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i][j]: whether s[i:j] is palidromic
        # to measure dp[i][j] we need dp[i + 1][j - 1]
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        count = 0
        for i in range(n - 1, -1, -1):#so that [i + 1] is valid
            for j in range(i, n):#so that dp[j - 1] is valid
                if s[i] == s[j]:#must the same
                    if j - i < 2 or dp[i + 1][j - 1]:#could be length 2 or more
                        dp[i][j] = True
                        count += 1
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna