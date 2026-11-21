class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 10**9 + 7
        cols = min(arrLen, steps // 2 + 1)
        dp = [[0] * cols for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(cols):
                dp[i][j] = dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j < cols - 1:
                    dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= MOD
        return dp[-1][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna