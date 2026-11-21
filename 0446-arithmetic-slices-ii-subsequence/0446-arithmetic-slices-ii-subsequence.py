class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # dp[i][j]: the number of arithmetic slices ends at i with difference d
        dp = [{} for _ in range(n)]
        ans = 0

        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                # find the ans
                cnt = dp[j].get(d, 0)
                ans += cnt
                # update [j,i] and dp[j][d](cnt) to dic
                dp[i][d] = dp[i].get(d, 0) + cnt + 1
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna