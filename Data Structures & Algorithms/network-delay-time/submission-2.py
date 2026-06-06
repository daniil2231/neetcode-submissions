class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x: [] for x in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((v, w))
        
        minh = [[0, k]]
        distances = [float("inf") for _ in range(n)]
        distances[k - 1] = 0
        seen = set()
        while minh:
            currDist, currNode = heapq.heappop(minh)
            if currNode in seen:
                continue
            seen.add(currNode)

            for neighbor, distToNeighbor in adj[currNode]:
                heapq.heappush(minh, [currDist + distToNeighbor, neighbor])
                distances[neighbor - 1] = min(distances[neighbor - 1], currDist + distToNeighbor)
        return max(distances) if max(distances) < float("inf") else -1