class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # monotonic stack: decrease val
        # default: 0
        n = len(temperatures)
        answer = [0] * n
        stack = []# indices

        for i, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna