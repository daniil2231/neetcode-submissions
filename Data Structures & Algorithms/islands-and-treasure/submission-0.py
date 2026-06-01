class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i, j):
            seen = set((i, j))
            q = collections.deque([[i, j, 0]])

            while q:
                r, c, dist = q.popleft()

                grid[r][c] = min(dist, grid[r][c])
                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] > 0 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append([nr, nc, dist + 1])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs(i, j)