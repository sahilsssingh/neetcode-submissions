class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        L = 0
        R = N - 1

        while L <= R:
            M = (L + R) // 2

            if matrix[M][0] > target:
                R = M - 1

            elif matrix[M][0] < target:
                if N == (M + 1) or matrix[M + 1][0] > target:
                    return self.searchRow(target, matrix, M)
                L = M + 1

            elif matrix[M][0] == target:
                return True

        return False
    
    def searchRow(self, target, matrix, M):
        n = len(matrix[M])
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[M][m] == target:
                return True

            elif matrix[M][m] > target:
                r = m - 1

            elif matrix[M][m] < target:
                l = m + 1
        
        return False
            