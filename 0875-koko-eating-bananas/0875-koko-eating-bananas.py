class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def count(speed):
            return sum((x + speed - 1) // speed for x in piles)#向上取整
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if count(mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna