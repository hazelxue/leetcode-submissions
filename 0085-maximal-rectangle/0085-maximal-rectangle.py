class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for row in matrix:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            max_area = max(max_area, self.largestrectanglearea(heights))
        return max_area
    
    def largestrectanglearea(self, heights):
        stack = [] # increasing:(start, val)
        max_area = 0
        for i, val in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] >= val:
                popi, poph = stack.pop()
                max_area = max(max_area, poph * (i - popi))
                start = popi
            stack.append((start, val))
        return max_area

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna