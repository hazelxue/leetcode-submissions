class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # find first index that index != val
        l, r = 0, len(nums) - 1
        res = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] != mid:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna