class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for dst, src in prerequisites:
            adj[src].append(dst)
            indeg[dst] += 1
        
        noIndeg = []
        res = []
        for i in range(len(indeg)):
            if indeg[i] == 0:
                noIndeg.append(i)
                res.append(i)
        
        while noIndeg:
            node = noIndeg.pop()

            for neighbor in adj[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    noIndeg.append(neighbor)
                    res.append(neighbor)
        
        return res if len(res) == numCourses else []