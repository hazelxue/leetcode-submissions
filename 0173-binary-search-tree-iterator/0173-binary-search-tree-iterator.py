# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []#已经过的点
        self.pull_left(root)
    
    def pull_left(self, node):#自己加的def，将要访问的点
        while node:
            self.stack.append(node)
            node = node.left#左

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()#中
        self.pull_left(node.right)#右
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna