from copy import deepcopy
maxRow, maxCol = 0, 0
with open('data.txt') as f:
#with open('example.txt') as f:
    for line in f.readlines():
        point1, point2 = line.split('->')
        r1, c1 = point1.split(',')
        r2, c2 = point2.split(',')
        maxRow = max(maxRow, int(r1), int(r2))
        maxCol = max(maxCol, int(c1), int(c2))
board = [[0 for _ in range(maxCol + 1)] for _ in  range(maxRow + 1)]
# print(maxRow, maxCol, board)

with open('data.txt') as f:
#with open('example.txt') as f:
    for line in f.readlines():
        point1, point2 = line.split('->')
        r1, c1 = point1.split(',')
        r2, c2 = point2.split(',')
        #r1, c1 = maxRow - int(x1), int(y1)
        #r2, c2 = maxRow - int(x2), int(y2)
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
        if r1 == r2:
            print(r1,c1,r2,c2)
            for c in range(min(c1, c2), max(c1, c2) + 1):
                print(r1, c)
                board[r1][c] += 1
        elif c1 == c2:
            print(r1,c1,r2,c2)
            for r in range(min(r1, r2), max(r1, r2) + 1):
                board[r][c1] += 1

# print(board)

count = 0
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] >= 2:
            count += 1
print(count)
import numpy as np
print(np.matrix(board))