class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter_map = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"          
        ]

        path = []
        res = []

        def backtracking(index):
            if len(digits) == index:
                res.append("".join(path))
                return
            letter = letter_map[int(digits[index])]
            for ch in letter:
                path.append(ch)
                backtracking(index + 1)
                path.pop()
        
        backtracking(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna