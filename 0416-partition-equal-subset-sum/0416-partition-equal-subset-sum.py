class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums) // 2
        if sum(nums) % 2 == 1:
            return False
        
        m = len(nums)
        dp = [[False] * (target + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            x = nums[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] = dp[i - 1][j - x] or dp[i - 1][j]
        return dp[m][target]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna