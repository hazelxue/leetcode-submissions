# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        prev = [None]
        def dfs(root):
            if not root:
                return True
            if not dfs(root.left):
                return False
            if prev[0] is not None and root.val <= prev[0]:
                return False
            prev[0] = root.val
            return dfs(root.right)
        
        return dfs(root)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna