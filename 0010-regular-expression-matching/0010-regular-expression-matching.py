class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # 0 len p cannot match s
        # initialize p to match 0 len s
        for j in range(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        
        def match(a, b):
            return s[a] == p[b] or p[b] == '.'
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = match(i - 1, j - 1) and dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if match(i - 1, j - 2):
                        dp[i][j] = dp[i - 1][j] or dp[i][j]
        return dp[m][n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna