class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        n = len(maxHeights)
        left = [0] * n
        right = [0] * n
        max_h = 0

        stack = []# increasing
        for j in range(n):
            while stack and maxHeights[stack[-1]] >= maxHeights[j]:
                stack.pop()
            p = stack[-1] if stack else -1
            left[j] = (j - p) * maxHeights[j]
            if p != -1:
                left[j] += left[p]
            stack.append(j)
        
        stack = []# increasing
        for j in range(n - 1, -1, -1):
            while stack and maxHeights[stack[-1]] >= maxHeights[j]:
                stack.pop()
            p = stack[-1] if stack else n
            right[j] = (p - j) * maxHeights[j]
            if p != n:
                right[j] += right[p]
            stack.append(j)
        
        for i in range(n):
            level = left[i] + right[i] - maxHeights[i]
            max_h = max(max_h, level)
        return max_h


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna