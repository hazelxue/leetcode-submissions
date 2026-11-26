class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []# max val of each chunk, increasing
        for num in arr:
            max_val = num
            while stack and stack[-1] > num:
                max_val = max(max_val, stack.pop())
            stack.append(max_val)
        return len(stack)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna