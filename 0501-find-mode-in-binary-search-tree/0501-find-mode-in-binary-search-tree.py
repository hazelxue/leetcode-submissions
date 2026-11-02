# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)#left

            #middle
            if node.val == self.prev:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.max_count:
                self.max_count = self.count
                self.res = [node.val]
            elif self.count == self.max_count:
                self.res.append(node.val)
            self.prev = node.val
            
            dfs(node.right)#right
        
        dfs(root)
        return self.res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna