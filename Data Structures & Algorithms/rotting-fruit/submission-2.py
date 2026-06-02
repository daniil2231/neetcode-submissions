class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        fresh -= 1
                        q.append([nr, nc])
                        grid[nr][nc] = 2
            time += 1
        return time if fresh == 0 else -1