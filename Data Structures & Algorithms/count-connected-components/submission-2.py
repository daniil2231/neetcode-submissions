class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {x: [] for x in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()
        q = deque()
        connected = 0
        for key in adj:
            if key not in seen:
                q.append(key)
                seen.add(key)
                while q:
                    node = q.popleft()

                    for neighbor in adj[node]:
                        if neighbor not in seen:
                            q.append(neighbor)
                            seen.add(neighbor)
                connected += 1
        return connected