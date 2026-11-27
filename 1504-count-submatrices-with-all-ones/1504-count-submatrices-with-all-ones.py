class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        # step 1: treat every row as a base of histogram
        for row in mat:
            for j in range(n):
                heights[j] = heights[j] + row[j] if row[j] == 1 else 0
            
            # step 2: DP
            # dp[j] = number of rectangles whose bottom-right corner is (row, j)
            # transition: dp[j] = dp[p](previous column that first strictly shorter than h) + (j - p) * row[j]
            # find p: monotonic stack, indices, increasing
            stack = []
            count = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                p = stack[-1] if stack else -1
                count[j] = (j - p) * heights[j]
                if p != -1:
                    count[j] += count[p]
                total += count[j]
                stack.append(j)
        return total
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna