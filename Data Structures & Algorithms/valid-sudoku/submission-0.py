class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Satırlar
        for row in board:
            seen = set()

            for i in row:
                if i == ".":
                    continue

                if i in seen:
                    return False

                seen.add(i)

        # Sütunlar
        for j in range(9):
            seen = set()

            for i in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        # 3x3 kutular
        kutular = {}

        for i in range(9):
            for j in range(9):

                if board[i][j] == ".":
                    continue

                k = (i // 3, j // 3)

                if k not in kutular:
                    kutular[k] = set()

                if board[i][j] in kutular[k]:
                    return False

                kutular[k].add(board[i][j])

        return True