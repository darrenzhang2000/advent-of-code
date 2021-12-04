from copy import deepcopy
with open('data.txt') as f:
    lines = f.read().split('\n')
    numbers = lines[0].split(',')
    numbers = [int(num) for num in numbers]
    boards = []
    board = []
    for i in range(2, len(lines) + 1):
        if i == len(lines) or not lines[i]:
            boards.append(deepcopy(board))
            board = []
        else:
            row = lines[i].split()
            row = [int(n) for n in row]
            board.append(row)

lastNumPlaced = 0
n = len(boards[0])
def checkForWin(board, cur):
    for i in range(n):
        for j in range(n):
            if board[i][j] == cur:
                board[i][j] = -board[i][j] if board[i][j] != 0 else float('inf')

    # check horizontals
    for i in range(n):
        count = 0
        score = 0
        for j in range(n):
            if board[i][j] == float('inf') or board[i][j] < 0:
                score += board[i][j]
                count += 1
        # print(count)
        if count == n:
            return (True, -score)
        

    # check verticals
    for j in range(n):
        count = 0
        score = 0
        for i in range(n):
            if board[i][j] == float('inf') or board[i][j] < 0:
                score += board[i][j]
                count += 1
        if count == n:
            return (True, -score)
    
    return False, 0
        
def placeNumber(board, num):
    global lastNumPlaced
    placed = False
    for i in range(n):
        for j in range(n):
            if board[i][j] == num:
                board[i][j] *= -1
                placed = True
                lastNumPlaced = num
    return placed

def computeUnmarkedNums(board):
    score = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != float('inf') and board[i][j] > 0:
                score += board[i][j]
    return score

def placeAndCheckBoardsForWin(boards, num):
    global answer
    boardNum = 0
    for i, board in enumerate(boards):
        if placeNumber(board, num):
            isWinner, _ = checkForWin(board, num)
            if isWinner:
                if i in hasNotWonSet:
                    hasNotWonSet.remove(i)
                    if len(hasNotWonSet) == 0 and answer == 0:
                        answer = computeUnmarkedNums(board) * lastNumPlaced
                
        boardNum += 1
    return False, 0

def drawNumbers(arr):
    for num in arr:
        placeAndCheckBoardsForWin(boards, num)

answer = 0
hasNotWonSet = set(range(len(boards)))
unmarkedNumbersSum = drawNumbers(numbers)
print(answer)
# import numpy as np
# for board in boards:
#     print(np.matrix(board))
