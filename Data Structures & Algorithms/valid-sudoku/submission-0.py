class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        U: 
            input = 9x9 board 
            output = True if sudoku board is valid, false otherwise
            board 9/9 / 3 = 3x3 for each square
        P:
            col = set
            row = set
            box = set
            for r in 9:
                for c in 9:
                    if board[r][c] == '.':
                        continue
                    boxes = (r // 3, c // 3)
                    if board[r][c] in row[r] or ...
                        return false
                    add to row, col, box
            return True
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                box_vals = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in box[box_vals]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                box[box_vals].add(val)
        return True
            
        
