class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = nums + nums
        stack = []# decrease
        res = [-1] * (n * 2)

        for i in range(n * 2):
            while stack and nums[i] > nums[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = nums[i]
            stack.append(i)
        return res[:n]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna