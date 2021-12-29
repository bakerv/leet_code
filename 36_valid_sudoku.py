import time
import collections

class Solution(object):
    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        initial_values = []
        for row_index, row in enumerate(board):
            for col_index, entry in enumerate(row):
                if entry != '.':
                    initial_values.append(
                        [(row_index, entry),
                         (entry, col_index),
                         (row_index // 3, col_index // 3, entry)])

        initial_values = sum(initial_values, [])

        return len(initial_values) == len(set(initial_values))

test = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

counter = 0
start_time = time.time()
while counter < 100000:
    test.isValidSudoku1(board)
    counter +=1
print('Elapsed Time (seconds):', time.time() - start_time)


