class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def bfs(i, j):
            q = collections.deque([[i, j]])
            seen = set((i, j))

            while q:
                r, c = q.popleft()

                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O" and (nr, nc) not in seen:
                        q.append([nr, nc])
                        seen.add((nr, nc))
                        notSurrounded.add((nr, nc))

        notSurrounded = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                notSurrounded.add((r, 0))
                bfs(r, 0)
            if board[r][COLS - 1] == "O":
                notSurrounded.add((r, COLS - 1))
                bfs(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                notSurrounded.add((0, c))
                bfs(0, c)
            if board[ROWS - 1][c] == "O":
                notSurrounded.add((ROWS - 1, c))
                bfs(ROWS - 1, c)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in notSurrounded:
                    board[i][j] = "X"