class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x: x[0])
        heap = []
        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i][0]:
                heapq.heapreplace(heap, intervals[i][1])
            else:
                heapq.heappush(heap, intervals[i][1])
        return len(heap)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna