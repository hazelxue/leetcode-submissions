import random

class Solution(object):
    def __init__(self, w):
        # prefix[i] = sum of w[0..i], the right end of index i's segment
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)   # both ends inclusive

        # Find the first prefix sum >= target
        l, r = 0, len(self.prefix) - 1
        res = r
        while l <= r:
            mid = (l + r) // 2
            if self.prefix[mid] >= target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna