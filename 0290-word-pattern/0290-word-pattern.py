class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        p_to_word = {}
        word_to_p = {}
        for i, j in zip(pattern, words):
            if i in p_to_word and p_to_word[i] != j:
                return False
            if j in word_to_p and word_to_p[j] != i:
                return False
            p_to_word[i] = j
            word_to_p[j] = i
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna