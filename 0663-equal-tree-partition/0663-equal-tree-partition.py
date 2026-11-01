# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        sum_ = []
        def dfs(node):
            if not node:
                return 0
            #后序
            l = dfs(node.left)
            r = dfs(node.right)
            sum_.append(node.val + l + r)

            return node.val + l + r
        
        dfs(root)
        if sum_[-1] / 2.0 in sum_[: -1]:#不能包含最后一位，他自己是整棵树，2.0避免了是奇数的情况
            return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna