class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isNthRowValid(n: int):
            s = set()
            for num in board[n]:
                if num.isdigit():
                    if num in s:
                        return False
                    s.add(num)
            return True
        def isNthColValid(n: int):
            s = set()
            for num in [row[n] for row in board]:
                if num.isdigit():
                    if num in s:
                        return False
                    s.add(num)
            return True

        def is3By3CellsValid(row, col):
            s = set()
            for r in board[row:row + 3]:
                for c in r[col: col + 3]:
                    if c.isdigit():
                        if c in s:
                            return False
                        s.add(c)

            return True

        def getRowAndCol(n):
            if n == 1:
                return (0, 0)
            if n == 2:
                return (0, 0 + 2 + 1)
            if n == 3:
                return (0, 0 + 2 + 1 + 2 + 1)
            if n == 4:
                return (3, 0)
            if n == 5:
                return (3, 0 + 2 + 1)
            if n == 6:
                return (3, 0 + 2 + 1 + 2 + 1)
            if n == 7:
                return (6, 0)
            if n == 8:
                return (6, 0 + 2 + 1)
            if n == 9:
                return (6, 0 + 2 + 1 + 2 + 1)
            return (0, 0)

        for i in range(1, 10):
            [row, col] = getRowAndCol(i)
            if not is3By3CellsValid(row, col):
                return False
            
            if not isNthRowValid(i - 1):
                return False

            if not isNthColValid(i - 1):
                return False

        return True









