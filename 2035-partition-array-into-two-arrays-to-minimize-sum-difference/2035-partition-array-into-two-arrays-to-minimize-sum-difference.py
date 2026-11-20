from bisect import bisect_left
from itertools import combinations

class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total = sum(nums)
        L, R = nums[:n], nums[n:]
        res = float('inf')

        for i in range(n + 1):
            l = [sum(x) for x in combinations(L, i)]
            r = sorted([sum(x) for x in combinations(R, n - i)])
            for j in l:
                idx = bisect_left(r, (total - 2 * j) / 2)
                for k in [idx, idx - 1]:
                    if 0 <= k < len(r):
                        res = min(res, abs(total - 2 * (j + r[k])))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna