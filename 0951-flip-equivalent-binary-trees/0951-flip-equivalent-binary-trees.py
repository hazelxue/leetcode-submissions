# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        a, b = root1, root2
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or
        (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna