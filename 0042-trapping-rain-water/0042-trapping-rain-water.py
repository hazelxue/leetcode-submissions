class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        lmax = height[l]
        rmax = height[r]
        rain = 0
        while l < r:
            if lmax < rmax:
                l += 1
                rain += max(0, lmax - height[l])
                lmax = max(lmax, height[l])
            else:
                r -= 1
                rain += max(0, rmax - height[r])
                rmax = max(rmax, height[r])
        return rain


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna