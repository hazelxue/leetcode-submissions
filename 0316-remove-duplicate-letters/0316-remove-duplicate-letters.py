class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)
        seen = set()
        last = {ch: i for i, ch in enumerate(s)}
        for i in range(n):
            if s[i] in seen:
                continue
            while stack and stack[-1] > s[i] and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna