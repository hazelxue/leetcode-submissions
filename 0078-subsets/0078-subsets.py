class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path = []
        result = []
        
        def backtracking(nums, start_index):
            result.append(path[:])
            if start_index >= len(nums):
                return
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)# not start_index + 1
                path.pop()
        
        backtracking(nums, 0)
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna