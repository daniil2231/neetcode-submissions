class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            q = collections.deque([[i, j]])
            while q:
                r, c = q.popleft()

                for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        q.append([nr, nc])
                        seen.add((nr, nc))

        res = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    res += 1
                    seen.add((i, j))
                    bfs(i, j)
        
        return res