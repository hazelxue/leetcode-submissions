class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        # dp[i][j][c]: number of arrs when length i, max value j, search cost c
        # when len = 1, search cost = 1
        for j in range(1, m + 1):
            dp[1][j][1] = 1
        
        # j not max: dp[i - 1][j][c] * j
        # j is max: dp[i - 1][1][c - 1]+...+dp[i - 1][j - 1][c - 1]
        # i, c should be top-bottom, j should be left-to-right in innermost loop, i should be outermost loop
        for i in range(2, n + 1):
            for c in range(1, k + 1):
                prefix = 0
                for j in range(1, m + 1):
                    dp[i][j][c] = (dp[i - 1][j][c] * j + prefix) % MOD
                    prefix += dp[i - 1][j][c - 1] % MOD
        res = 0
        for j in range(1, m + 1):
            res += dp[-1][j][-1]
        return res % MOD

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna