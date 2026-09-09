class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hash_set = set()
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def backtrack(i, j, l):
            if l == len(word):
                return True
        
            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == word[l] and (ni, nj) not in hash_set:
                    hash_set.add((ni, nj))
                    if backtrack(ni, nj, l + 1):
                        return True
                    hash_set.discard((ni, nj))
            
            return False
    
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j]:
                    hash_set.add((i, j))
                    if backtrack(i, j, 1):
                        return True
                    hash_set.discard((i, j))

        return False