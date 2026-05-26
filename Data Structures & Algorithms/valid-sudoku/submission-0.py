from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check all the rows
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        # check all the cols
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # check for sub squares
        squares = {} #(r/3, col/3): set()
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                cord = (row//3, col//3)
                if cord not in squares:
                    squares[cord] = set()
                
                if board[row][col] in squares[cord]:
                    return False
                squares[cord].add(board[row][col])
        
        return True

        

        