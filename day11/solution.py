import os
import numpy as np

numFlashes = 0
def flashAndIncrementNeighbors(mat, hasFlashed, r, c):
    if hasFlashed[r][c]:
        return
    hasFlashed[r][c] = True
    global numFlashes
    numFlashes += 1
    mat[r][c] += 1
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in neighbors:
        if 0 <= r + dr < len(mat) and 0 <= c + dc < len(mat[0]):
            mat[r + dr][c + dc] += 1
            if mat[r + dr][c + dc] >= 10:
                flashAndIncrementNeighbors(mat, hasFlashed, r + dr, c + dc) 

def solution(mat):
    for _ in range(100):
        hasFlashed = [[False for _ in range(len(mat))] for _ in range(len(mat[0]))]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat[r][c] += 1
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 10:
                    flashAndIncrementNeighbors(mat, hasFlashed, r, c)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] > 9:
                    mat[r][c] = 0
    print(numFlashes, np.array(mat))
    return numFlashes, mat

def allFlashed(mat):
    return all(mat[r][c] for r in range(len(mat)) for c in range(len(mat[0])))

def solution2(mat):
    for step in range(300):
        hasFlashed = [[False for _ in range(len(mat))] for _ in range(len(mat[0]))]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat[r][c] += 1
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 10:
                    flashAndIncrementNeighbors(mat, hasFlashed, r, c)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] > 9:
                    mat[r][c] = 0

        if allFlashed(hasFlashed):
            return step + 1


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, 'data.txt')) as file:
        data = file.read().splitlines()
        data = [[int(n) for n in row] for row in data]
        print(data)
        #solution(data)
        print(solution2(data))

