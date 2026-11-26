class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        stack = []#increasing: (i, val)
        for i, val in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= val:
                popi, poph = stack.pop()
                max_area = max(max_area, poph * (i - popi))
                start = popi
            stack.append((start, val))
        for i, val in stack:
            max_area = max(max_area, (len(heights) - i) * val)
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna