# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:#equal
            if not root.left:#left is empty
                return root.right
            elif not root.right:#right is empty
                return root.left
            else:#both not empty
                cur = root.right
                while cur.left:
                    cur = cur.left #find the smallest one in this subtree
                root.val = cur.val#copy its value to the root
                #delete cur
                root.right = self.deleteNode(root.right, cur.val)
        return root

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna