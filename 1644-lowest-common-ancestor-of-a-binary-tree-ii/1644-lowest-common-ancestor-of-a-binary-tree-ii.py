# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res = [0]
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node == p or node == q:
                res[0] += 1
                return node
            if l and r:
                return node
            return l or r
        ans = dfs(root)
        return ans if res[0] == 2 else None

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna