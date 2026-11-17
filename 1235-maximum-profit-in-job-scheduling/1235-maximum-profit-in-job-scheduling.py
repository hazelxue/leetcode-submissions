class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # sort by end time
        # 每个job的状态只有取和不取两种
        n = len(profit)
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # find endtime <= startTime[i]
            s, e, p = jobs[i - 1]
            l, r = 0, i - 2
            res = -1
            while l <= r:
                mid = (l + r) // 2
                if jobs[mid][1] <= s:
                    l = mid + 1
                    res = mid
                else:
                    r = mid - 1
                
            dp[i] = max(dp[i - 1], p + dp[res + 1])
        
        return dp[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna