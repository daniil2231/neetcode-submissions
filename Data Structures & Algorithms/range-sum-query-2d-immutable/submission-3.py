class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rowPrefSums = matrix.copy()
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.rowPrefSums[i][j] = self.rowPrefSums[i][j] + self.rowPrefSums[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                res += self.rowPrefSums[i][col2]
            else:
                res += self.rowPrefSums[i][col2] - self.rowPrefSums[i][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)