# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        prev = [None]#存入节点，而不是val，否则后面交换点位就不好做了
        first = [None]
        second = [None]

        def dfs(node):
            if not node:
                return 
            dfs(node.left)

            if prev[0] and prev[0].val > node.val:
                if not first[0]:
                    first[0] = prev[0]
                second[0] = node
            prev[0] = node
            
            dfs(node.right)
        
        dfs(root)
        first[0].val, second[0].val = second[0].val, first[0].val
        return root


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna