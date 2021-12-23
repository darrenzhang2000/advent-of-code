import os
import statistics

openParenMap = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

errorPointsMap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
def calcErrorPts(s):
    stack = []
    for c in s:
        isOpenParen = c not in openParenMap
        if isOpenParen:
            stack.append(c)
        else:
            matchingOpenParen = openParenMap[c]
            if not stack or stack[-1] != matchingOpenParen:
                return errorPointsMap[c], stack
            else:
                stack.pop()
    return 0, stack

def solution(data):
    errorScore = 0
    for line in data:
        score, _ = calcErrorPts(line)
        errorScore += score 
    return errorScore

autoCompletePointsMap = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}
def computeAutocompleteScore(stack):
    score = 0
    for p in reversed(stack):
        score = 5 * score + autoCompletePointsMap[p]
    return score

def solution2(data):
    autocompleteScores = []
    for line in data:
        errorScore, stack = calcErrorPts(line)
        isIncomplete = errorScore == 0
        if isIncomplete:
            autocompleteScores.append(computeAutocompleteScore(stack))
    return statistics.median(autocompleteScores)


if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, 'data.txt')) as file:
        data = file.read().splitlines()
        print(solution(data))
        print(solution2(data))
