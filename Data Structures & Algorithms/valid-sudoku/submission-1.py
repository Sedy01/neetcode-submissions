class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                value = board[row][col]

                if value != ".":
                    square_index = (row // 3) * 3 + (col // 3)
                    if value in rows[row]:
                        return False
                    if value in columns[col]:
                        return False
                    if value in squares[square_index]:
                        return False
                    
                    rows[row].add(value)
                    columns[col].add(value)
                    squares[square_index].add(value)
        
        return True
