class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        seen = set([0])
        q = collections.deque([[0, -1]])
        while q:
            node, par = q.popleft()

            for neighbor in adj[node]:
                if neighbor != par and neighbor in seen:
                    return False
                if neighbor not in seen:
                    q.append([neighbor, node])
                    seen.add(neighbor)
        return len(seen) == n