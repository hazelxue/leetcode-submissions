class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr) - 2
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna