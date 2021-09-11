from typing import Collection


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # sets that will be used to hold the entries that already exist and entries we still
        # need to add info to
        rows, cols, trips, emptyEntry = Collection.defaultdict(set), Collection.defaultdict(set), Collection.defaultdict(set), []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    # if the board is already filled at this place, add it to the row, col,
                    # and trips sets
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    trips[(r // 3, c // 3)].add(board[r][c])
                    
                else:
                    # if there is not entry here add it to the emptyEntry list, which 
                    # indicates we need to add an entry to it
                    emptyEntry.append((r, c))
                    
        def solveSudokuHelper():
            # first checking to see if there's any more entries we need to add
            if not emptyEntry:
                return True
            # get the last entry in the emptyEntry list
            r, c = emptyEntry[-1]
            t = (r // 3, c // 3)

            for num in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if num not in rows[r] and num not in cols[c] and num not in trips[t]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    trips[t].add(num)
                    # now that we've added it, take it off
                    emptyEntry.pop()
                    # will now recursively call the function to see if the current entry we 
                    # added worked

                    if solveSudokuHelper():
                        return True

                    else:
                        # if the entries didn't work out, take it off the board and the
                        # rows, columns, and triples list and put it back on the emptyEntry
                        # list
                        board[r][c] = "."
                        rows[r].discard(num)
                        cols[c].discard(num)
                        trips[t].discard(num)
                        emptyEntry.append((r, c))

            return False
        solveSudokuHelper()