class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp[i] = how manys ways that i can be decoded
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna