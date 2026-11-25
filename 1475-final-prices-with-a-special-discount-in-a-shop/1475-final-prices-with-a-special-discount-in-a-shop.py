class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = [] # indices waiting for lower vaule # increase
        res = prices[:] # default: no discount

        for i, val in enumerate(prices):
            while stack and prices[stack[-1]] >= val:
                tmp = stack.pop()
                res[tmp] = prices[tmp] - val
            stack.append(i)
        
        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna