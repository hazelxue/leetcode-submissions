class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        path = []
        res = []
        visited = [False] * len(nums)

        def backtracking():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtracking()
                path.pop()
                visited[i] = False
        
        backtracking()
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna