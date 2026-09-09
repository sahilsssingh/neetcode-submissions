class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hash_set = set()

        def backtrack(i, j, l):
            if l == len(word):
                return True
        
            #left
            if j > 0 and board[i][j - 1] == word[l] and (i, j - 1) not in hash_set:
                hash_set.add((i, j - 1))
                if backtrack(i, j - 1, l + 1):
                    return True
                hash_set.discard((i, j - 1))
                        
            #right
            if j < len(board[i]) - 1 and board[i][j + 1] == word[l] and (i, j + 1) not in hash_set:
                hash_set.add((i, j + 1))
                if backtrack(i, j + 1, l + 1):
                    return True
                hash_set.discard((i, j + 1))

            #up
            if i > 0 and board[i - 1][j] == word[l] and (i - 1, j) not in hash_set:
                hash_set.add((i - 1, j))
                if backtrack(i - 1, j, l + 1):
                    return True
                hash_set.discard((i - 1, j))

            #down
            if i < len(board) - 1 and board[i + 1][j] == word[l] and (i + 1, j) not in hash_set:
                hash_set.add((i + 1, j))
                if backtrack(i + 1, j, l + 1):
                    return True
                hash_set.discard((i + 1, j))
            
            return False
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    hash_set.add((i, j))
                    if backtrack(i, j, 1):
                        return True
                    hash_set.discard((i, j))

        return False