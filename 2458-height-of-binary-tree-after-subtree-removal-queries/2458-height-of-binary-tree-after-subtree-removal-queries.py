# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        # 1. dfs for d, h
        depth = {}
        height = {}
        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            h = 1 + max(dfs(node.left, d + 1), dfs(node.right, d + 1))
            height[node.val] = h
            return h

        # 2. get top2 dict
        dfs(root, 0)
        top = defaultdict(list)#depth: d + h, val
        for val, d in depth.items():
            top[d].append((d + height[val], val))#key could be invaild -> defaultdict
            top[d].sort(reverse=True)
            top[d] = top[d][:2]
        
        # 3. where is q(1st, 2sd, only item)
        res = []
        for q in queries:
            d = depth[q]
            if top[d][0][1] != q:
                res.append(top[d][0][0])
            else:
                if len(top[d]) > 1:
                    res.append(top[d][1][0])
                else:
                    res.append(d - 1)#not top[d][0][0] - 1, we delete children from q
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna