from typing import List
import pandas as pd

class Solution:

    def isValidList(self, row: List[str]) -> bool:
        row_clean = [int(x) for x in row if x != '.']

        seen = {}

        for elm in row_clean:
            if elm not in range(1,10):
                # print('There\'s a number not in 1 to 9')
                return False
            else:
                if elm not in seen:
                    seen[elm] = 1
                else:
                    # print('A number is repeating')
                    return False
        return True

    # def flatten(self, xss: List[int]) -> List[int]:
        # return [x for xs in xss for x in xs]

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for linha in board:
            if self.isValidList(linha):
                pass
            else:
                return False

        tboard = [list(group) for group in zip(*board)]

        for linha in tboard:
            if self.isValidList(linha):
                pass
            else:
                return False

        subgrids = []

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[box_row + i][box_col + j])
                subgrids.append(box)

        # for idx, grid in enumerate(subgrids):
            # print(f"Subgrid {idx+1}: {grid}")

        for linha in subgrids:
            if self.isValidList(linha):
                pass
            else:
                return False

        return True

s = Solution()
print(s.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    ))

