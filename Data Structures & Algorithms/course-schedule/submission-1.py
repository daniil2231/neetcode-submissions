class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {x: [] for x in range(numCourses)}
        inc = {x: 0 for x in range(numCourses)}
        for dst, src in prerequisites:
            if adj.get(src, []) == []:
                adj[src] = [dst]
            else:
                adj[src].append(dst)
            inc[dst] += 1

        noInc = []
        for k in inc:
            if inc[k] == 0:
                noInc.append(k)
        
        done = 0
        while noInc:
            node = noInc.pop()
            for neighbor in adj[node]:
                inc[neighbor] -= 1
                if inc[neighbor] == 0:
                    noInc.append(neighbor)
            done += 1
        return done == numCourses