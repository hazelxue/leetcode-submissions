class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        res = []
        for p in points:
            d = p[0] * p[0] + p[1] * p[1]
            heapq.heappush(heap, (d, p))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna