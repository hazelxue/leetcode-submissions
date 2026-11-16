# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[Optional[TreeNode]]
        """
        dic = {} #str(4,1,#,#):time
        res = []
        def dfs(node):
            if not node:
                return '#'
            l = dfs(node.left)
            r = dfs(node.right)
            #mid
            s = str(node.val) + ',' + l + ',' + r
            dic[s] = dic.get(s, 0) + 1
            if dic[s] == 2:
                res.append(node)
            return s
        dfs(root)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna