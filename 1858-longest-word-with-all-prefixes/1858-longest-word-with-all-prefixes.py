class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()# a ap app appl
        valid = {""}#words with all prefixes # a set containing the empty string
        ans = ""

        for word in words:
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna