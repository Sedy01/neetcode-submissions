class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rows = {}
            for j in range(len(board[i])):
                value = board[i][j]
                if value != ".":
                    if value not in rows:
                        rows[value] = 1
                    else:
                        rows[value] += 1
                    if rows[value] > 1:
                        return False

        for j in range(len(board[0])):
            columns = {}
            for i in range(len(board)):
                value = board[i][j]
                if value != ".":
                    if value not in columns:
                        columns[value] = 1
                    else:
                        columns[value] += 1
                    if columns[value] > 1:
                        return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                square = {}

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        value = board[i][j]
                        if value != ".":
                            if value not in square:
                                square[value] = 1
                            else: square[value] += 1
                            if square[value] > 1:
                                return False
        
        return True
