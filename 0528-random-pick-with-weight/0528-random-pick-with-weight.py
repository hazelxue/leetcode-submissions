import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        # prefix[i] = w[0] + ... + w[i]
        # Index i owns the range (prefix[i-1], prefix[i]] on a number line,
        # so its length equals its weight.
        self.prefix = [w[0]]
        for n in w[1:]:
            self.prefix.append(self.prefix[-1] + n)   # running sum so far

    def pickIndex(self):
        """
        :rtype: int
        """
        # Pick a random point on the line [1, total]
        target = random.randint(1, self.prefix[-1])

        # Binary search for the first prefix sum >= target;
        # that index's segment contains the random point
        l, r = 0, len(self.prefix) - 1
        res = r     # Never actually used: prefix[-1] == total >= target
        while l <= r:
            mid = (l + r) // 2
            if self.prefix[mid] >= target:
                res = mid       # mid is a candidate, look further left
                r = mid - 1
            else:
                l = mid + 1     # prefix[mid] too small, go right
        return res

# __init__:  O(n) time, O(n) space
# pickIndex: O(log n) time

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna