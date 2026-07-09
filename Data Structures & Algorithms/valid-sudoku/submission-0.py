class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0 , 9):
            hash_dict = {}
            for j in range(0 , 9):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False
        
        for j in range(0 , 9):
            hash_dict = {}
            for i in range(0 , 9):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(0 , 3):
            for j in range(0 , 3):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(0 , 3):
            for j in range(3 , 6):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(0 , 3):
            for j in range(6 , 9):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(3 , 6):
            for j in range(0 , 3):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(3 , 6):
            for j in range(3 , 6):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(3 , 6):
            for j in range(6 , 9):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(6 , 9):
            for j in range(0 , 3):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(6 , 9):
            for j in range(3 , 6):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        hash_dict = {}
        for i in range(6 , 9):
            for j in range(6 , 9):
                if board[i][j] != ".":
                    hash_dict[board[i][j]] = hash_dict.get(board[i][j] , 0) + 1
            for k , v in hash_dict.items():
                if v > 1:
                    return False

        return True