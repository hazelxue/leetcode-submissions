class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 == 1:
            return 0
        P = (total + target) // 2

        m = len(nums)
        dp = [[0] * (P + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m + 1):
            x = nums[i - 1]
            for j in range(P + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] += dp[i - 1][j - x]
        return dp[m][P]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna