"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        clone = {node: Node(node.val)}
        q = deque([node])
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                    q.append(n)
                clone[cur].neighbors.append(clone[n])
        return clone[node]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna