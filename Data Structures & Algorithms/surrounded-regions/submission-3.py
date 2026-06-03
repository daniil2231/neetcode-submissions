class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def bfs():
            q = collections.deque([])

            for r in range(ROWS):
                if board[r][0] == "O":
                    board[r][0] = "N"
                    q.append([r, 0])
                if board[r][COLS - 1] == "O":
                    board[r][COLS - 1] = "N"
                    q.append([r, COLS - 1])

            for c in range(COLS):
                if board[0][c] == "O":
                    board[0][c] = "N"
                    q.append([0, c])
                if board[ROWS - 1][c] == "O":
                    board[ROWS - 1][c] = "N"
                    q.append([ROWS - 1, c])

            seen = set()
            while q:
                r, c = q.popleft()

                for nr, nc in [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O" and (nr, nc) not in seen:
                        q.append([nr, nc])
                        seen.add((nr, nc))
                        board[nr][nc] = "N"

        bfs()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"