# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def dfs(node):
            if not node:
                return 0, None
            #l, r, m
            l_depth, l_node = dfs(node.left)
            r_depth, r_node = dfs(node.right)
            if l_depth > r_depth:
                return l_depth + 1, l_node
            elif l_depth < r_depth:
                return r_depth + 1, r_node
            else:
                return r_depth + 1, node
        return dfs(root)[1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna