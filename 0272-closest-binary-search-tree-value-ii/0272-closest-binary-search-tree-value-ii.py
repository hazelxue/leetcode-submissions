# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: Optional[TreeNode]
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        heap = []#(distance to target, val)
        # go through all nodes, but this don't use bst proporties?

        def dfs(node):
            if not node:
                return
            heapq.heappush(heap, (abs(target - node.val), node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return [heapq.heappop(heap)[1] for i in range(k)]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna