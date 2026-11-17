class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # dp：走到这里的最小累计和
        
        dp = []
        n = len(triangle)
        dp.append(triangle[0])

        for i in range(1, n):
            level = []
            for j in range(i + 1):
                p1 = dp[-1][j] if j < i else float('inf')
                p2 = dp[-1][j - 1] if j != 0 else float('inf')
                level.append(triangle[i][j] + min(p1, p2))
            dp.append(level)
        return min(dp[-1])

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna