class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)#not [] but list
        pre = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)#[pre_course, course]
            pre[a] += 1
        
        q = deque([i for i in range(len(pre)) if pre[i] == 0])
        take = []
        while q:
            tmp = q.popleft()
            take.append(tmp)
            for c in graph[tmp]:
                pre[c] -= 1
                if pre[c] == 0:
                    q.append(c)
        return take if len(take) == numCourses else []

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna