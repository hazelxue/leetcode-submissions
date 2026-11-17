class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0],
        7: [2, 6], 8: [1, 3], 9: [2, 4]}
        dp = [[1] * 10 for _ in range(n)]
        for i in range(1, n):
            for j in range(10):
                dp[i][j] = sum(dp[i - 1][x] for x in moves[j]) % MOD
        return sum(dp[-1]) % MOD


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna