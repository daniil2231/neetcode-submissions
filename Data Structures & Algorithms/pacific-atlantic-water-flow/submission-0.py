class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(i, j):
            q = collections.deque([[i, j]])
            pReached, aReached = False, False
            seen = set((i, j))

            while q:
                r, c = q.popleft()

                if r == 0 or c == 0:
                    pReached = True
                if r == len(heights) - 1 or c == len(heights[0]) - 1:
                    aReached = True
                
                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in seen and heights[r][c] >= heights[nr][nc]:
                        q.append([nr, nc])
                        seen.add((nr, nc))
            
            if pReached and aReached:
                res.append([i, j])

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                bfs(i, j)
        return res