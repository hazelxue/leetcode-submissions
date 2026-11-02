# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        path = []
        res = []

        def dfs(node, sum_):
            #end
            if not node:
                return
            #middle, collect res
            path.append(node.val)
            sum_ = sum_ + node.val
            
            if sum_ == targetSum and not node.left and not node.right:   
                res.append(path[:])# do not return before pop(), in recursion every append need pop

            #left
            dfs(node.left, sum_)
            #right
            dfs(node.right, sum_)
            path.pop()

        dfs(root, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna