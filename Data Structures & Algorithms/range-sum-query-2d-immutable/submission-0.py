class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.sumMat = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        totalBox = self.sumMat[row2][col2]
        upperTotal = self.sumMat[row1 - 1][col2]
        leftTotal = self.sumMat[row2][col1 - 1]
        extra = self.sumMat[row1 - 1][col1 - 1]

        return totalBox - upperTotal - leftTotal + extra

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)