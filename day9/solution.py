import os


def solution(board):
    riskLevel = 0
    m, n = len(board), len(board[0])
    for r in range(m):
        for c in range(n):
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            isLowPoint = True
            for offset in offsets:
                outOfBounds = not (0 <= r + offset[0] < m and 0 <= c + offset[1] < n)
                if not outOfBounds:
                    if not int(board[r][c]) < int(board[r + offset[0]][c + offset[1]]):
                        isLowPoint = False
            if isLowPoint:
                riskLevel += 1 + int(board[r][c])
    return riskLevel

def getBasinSize(board, r, c, visited):
    m, n = len(board), len(board[0])
    size = 0
    stack = [(r, c)]
    while stack:
        row, col = stack.pop()
        size += 1
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in offsets:
            newR, newC = row + dr, col + dc
            inBounds = (0 <= newR < m and 0 <= newC < n)
            if inBounds and board[newR][newC] != '9' and (newR, newC) not in visited:
                visited.add((newR, newC))
                stack.append((newR, newC))
    return size


def solution2(board):
    m, n = len(board), len(board[0])
    visited = set()
    basins = []
    for r in range(m):
        for c in range(n):
            if (r, c) not in visited and board[r][c] != '9':
                visited.add((r, c))
                basins.append(getBasinSize(board, r, c, visited))
                
    basins = sorted(basins, reverse=True)
    # print(basins)
    return basins[0] * basins[1] * basins[2]

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, 'data.txt')) as file:
        data = file.read().splitlines()
        print(solution(data))
        print(solution2(data))
