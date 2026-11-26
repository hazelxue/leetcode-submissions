class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and stack[-1] > s[i] and stack[-1] in s[i:]:
                stack.pop()
            stack.append(s[i])
        return "".join(stack)

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna