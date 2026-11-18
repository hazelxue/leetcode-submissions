class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = max(nums) + 1
        tree = [0] * (size * 2)

        def update(i, val):
            i += size
            tree[i] = max(tree[i], val)
            while i > 1:
                i //= 2
                tree[i] = max(tree[i * 2], tree[i * 2 + 1])

        def query(l, r):
            res = 0
            l += size
            r += size + 1#[l, r)
            while l < r:
                if l % 2 == 1:
                    res = max(res, tree[l])
                    l += 1
                if r % 2 == 1:
                    r -= 1
                    res = max(res, tree[r])
                l //= 2
                r //= 2
            return res
        
        ans = 0
        for num in nums:
            tmp = query(max(0, num - k), num - 1) + 1
            update(num, tmp)
            ans = max(ans, tmp)
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna