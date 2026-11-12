class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxlen = 0
        for num in nums:
            if num - 1 not in nums:
                curlen = 1
                while num + 1 in nums:
                    curlen += 1
                    num += 1
                maxlen = max(maxlen, curlen)
        return maxlen



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna