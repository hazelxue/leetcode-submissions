# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def dfs(node, depth):
            if not node:
                return
            #middle
            if depth == len(res):
                res.append(node.val)#first val in this depth
            else:
                if node.val > res[depth]:
                    res[depth] = node.val
            #left
            if node.left:
                dfs(node.left, depth + 1)
            #right
            if node.right:
                dfs(node.right, depth + 1)
        dfs(root, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna