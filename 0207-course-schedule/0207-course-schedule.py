class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        pre = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            pre[a] += 1
        
        q = deque([i for i in range(len(pre)) if pre[i] == 0])
        take = 0
        while q:
            tmp = q.popleft()
            take += 1
            for c in graph[tmp]:
                pre[c] -= 1
                if pre[c] == 0:
                    q.append(c)
        return True if take == numCourses else False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna