class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # dp[i]: sum, min val that subarry ends at i, starts from 0-i
        # find the first nums[j] < nums[i], then dp[i] = dp[j] + nums[i] * (i - j)
        n = len(arr)
        dp = [0] * n
        stack = []# help find j in On time, store idx
        MOD = 10 ** 9 + 7

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            idx = stack[-1] if stack else -1
            dp[i] = (dp[idx] if idx >= 0 else 0) + (i - idx) * arr[i]
            stack.append(i)
        
        return sum(dp) % MOD


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna