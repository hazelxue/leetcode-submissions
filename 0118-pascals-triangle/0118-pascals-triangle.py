class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows + 1):
            level = [1] * i
            if i > 2:#可以删掉。
            # i = 1 或 i = 2 时，range(1, 0) 和 range(1, 1) 都是空的，循环本来就不会执行
                for j in range(1, i - 1):
                    level[j] = res[-1][j] + res[-1][j - 1]
            res.append(level)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna