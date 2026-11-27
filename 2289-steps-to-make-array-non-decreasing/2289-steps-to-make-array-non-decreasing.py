class Solution(object):
    def totalSteps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []#(val, step), decreasing
        max_step = 0
        for num in nums:
            cur = 0
            while stack and stack[-1][0] <= num:
                popval, popstep = stack.pop()
                cur = max(cur, popstep)
            if stack:
                cur += 1
                max_step = max(max_step, cur)
            else:
                cur = 0
            stack.append((num, cur))
        return max_step

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna