class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        seen = {1}
        for _ in range(n - 1):
            x = heapq.heappop(heap)
            for num in [2, 3, 5]:
                if num * x not in seen:
                    seen.add(num * x)
                    heapq.heappush(heap, num * x)
        return heap[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna