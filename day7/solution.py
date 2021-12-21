import os
from statistics import median

def solution(positions):
    bestPos = median(positions)
    return int(sum(abs(bestPos - pos) for pos in positions))

def solution2(positions):
    minCost = float('inf')
    for startPos in range(min(positions), max(positions)):
        cost = 0
        for otherPos in positions:
            diff = abs(startPos - otherPos)
            cost += diff * (diff + 1) / 2
        minCost = min(minCost, cost)
    return int(minCost)

if __name__ == "__main__":
    with open('data.txt') as file:
        data = file.read().splitlines()
        positions = [int(n) for n in data[0].split(',')]
    print(solution2(positions))