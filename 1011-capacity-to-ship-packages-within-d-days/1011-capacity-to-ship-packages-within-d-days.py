class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def count_days(speed):
            day = 1
            sum_ = 0
            for w in weights:
                sum_ += w
                if sum_ > speed:
                    day += 1
                    sum_ = w

            return day
        
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if count_days(mid) <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna