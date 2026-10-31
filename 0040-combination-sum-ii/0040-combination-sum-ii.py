class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        path = []
        res = []

        def backtracking(start_index, sum_):
            if sum_ == target:
                res.append(path[:])
                return
            for i in range(start_index, len(candidates)):
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                if sum_ + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtracking(i + 1, sum_ + candidates[i])
                path.pop()
        
        backtracking(0, 0)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna