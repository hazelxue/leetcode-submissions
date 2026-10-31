class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def backtracking(candidates, target, start_index, sum_):

            if sum_ == target:
                res.append(path[:])
                return
            elif sum_ > target:
                return
            for i in range(start_index, len(candidates)):
                path.append(candidates[i])
                backtracking(candidates, target, i, sum_ + path[-1])
                path.pop()
        
        backtracking(candidates, target, 0, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna