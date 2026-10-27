class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 2
        res = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] != nums[mid ^ 1]:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return nums[res]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna