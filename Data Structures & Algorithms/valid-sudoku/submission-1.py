class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for i in range(9):
            s_row = [0] * 10
            s_col = [0] * 10
            for j in range(9):
                if board[i][j] != ".":
                    if s_row[int(board[i][j])] == 0:
                        s_row[int(board[i][j])] = 1
                    else:
                        return False
                if board[j][i] != ".":        
                    if s_col[int(board[j][i])] == 0:
                        s_col[int(board[j][i])] = 1
                    else:
                        return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = [0] * 10
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] == ".":
                            continue
                        if s[int(board[i + k][j + l])] == 0:
                            s[int(board[i + k][j + l])] = 1
                        else:
                            return False

        return True