# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # get in-order list
        val = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            val.append(node.val)
            inorder(node.right)
        inorder(root)

        def build(l, r):
            if l > r:
                return
            mid = (l + r) // 2
            root = TreeNode(val[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(val) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna