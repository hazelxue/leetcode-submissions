class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # interval
        # dp[i][j] = the most difference in this interval(how much value one player can win)
        # if take left: dp[i + 1][j]
        # if take right: dp[i][j - 1]

        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # length is 1
        for i in range(n):
            dp[i][i] = nums[i]
        
        for i in range(n - 2, -1, -1):#bottom-up
            for j in range(i + 1, n):#front-back
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        return True if dp[0][n - 1] >= 0 else False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna