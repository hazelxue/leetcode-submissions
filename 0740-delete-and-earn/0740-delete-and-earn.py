class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        point = [0] * (m + 1)
        for num in nums:
            point[num] += num
        
        dp = [0] * (m + 1)
        dp[1] = point[1]
        for i in range(2, m + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + point[i])
        return dp[-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna