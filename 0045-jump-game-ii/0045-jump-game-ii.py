class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        cover = 0
        nxt = 0
        for i in range(len(nums) - 1):#for循环就可以，不用while
            nxt = max(nxt, i + nums[i])#先更新，再看是不是到头了
            if i == cover:
                step += 1
                cover = nxt
        return step

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna