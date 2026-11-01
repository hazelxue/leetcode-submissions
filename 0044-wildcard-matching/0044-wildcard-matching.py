class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):#do not start from n
                if p[j] == '*':
                    dp[i][j] = dp[i][j + 1] or (i < m and dp[i + 1][j])
                else:
                    dp[i][j] = (
                        i < m
                        and (p[j] == '?' or p[j] == s[i])
                        and dp[i + 1][j + 1]
                    )
        
        return dp[0][0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna