class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: x[0])
        queue = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= queue[-1][1]:
                queue[-1][1] = max(queue[-1][1], intervals[i][1])
            else:
                queue.append(intervals[i])
        return queue

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna