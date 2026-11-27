class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        total = 0

        for i in range(n):
            max_h = heights[i]
            level = max_h
            
            cur = max_h
            for j in range(i - 1, -1, -1):
                level += min(heights[j], cur)
                cur = min(heights[j], cur)
            
            cur = max_h
            for j in range(i + 1, n):
                level += min(cur, heights[j])
                cur = min(heights[j], cur)
            
            total = max(total, level)
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna