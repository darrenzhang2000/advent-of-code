import os
from collections import Counter

codes = [0 for _ in range(6)]

'''
found: 0, 1, 7, 

a - what 7 has that 1 doesn't have
9 - has all of 7 and numUniq = 6
e - what 8 has that 1, 4, 7, 9 don't have 
g - what 8 has that 1, 4, 7 don't have - exclude e
f - what all has that 2 doesn't have - 2 found
b, d - what 4 and 8 both have that 1 and 7 don't
c - for 1, now that f is found, only c is left
d - two should all be found except d
b - last one found that 8 doesn't have

acedgfb: 8 
cdfbe: 
gcdfa:
fbcad: 
dab: 7
cefabd:
cdfgeb"
eafb: 4
cagedb:
ab: 1
|
cdfeb fcadb cdfeb cdbaf
'''
segmentsCount = {
    0: 6,
    1: 2,  # unique
    2: 5,
    3: 5,
    4: 4,  # unique
    5: 5,
    6: 6,
    7: 3,  # unique
    8: 7,  # unique
    9: 6
}

numToStringMap = {n: "" for n in range(10)}
posTOCharMap = ["" for _ in range(7)]


def solution(data):
    count = 0
    for line in data:
        inp, outp = line.split('|')
        outpCombinations = outp.split()
        for combs in outpCombinations:
            combLen = len(set(combs))
            if combLen in [2, 4, 3, 7]:
                count += 1
    return (count)


def createSortedStringToNumMap(posTOCharMap):
    sortedStringToNumMap = {}
    zero = tuple(sorted(posTOCharMap[i] for i in [0,1,2,4,5,6]))
    sortedStringToNumMap[zero] = 0
    one = tuple(sorted(posTOCharMap[i] for i in [2,5]))
    sortedStringToNumMap[one] = 1
    two = tuple(sorted(posTOCharMap[i] for i in [0,2,3,4,6]))
    sortedStringToNumMap[two] = 2
    three = tuple(sorted(posTOCharMap[i] for i in [0,2,3,5,6]))
    sortedStringToNumMap[three] = 3
    four = tuple(sorted(posTOCharMap[i] for i in [1,2,3,5]))
    sortedStringToNumMap[four] = 4
    five = tuple(sorted(posTOCharMap[i] for i in [0,1,3,5,6]))
    sortedStringToNumMap[five] = 5
    six = tuple(sorted(posTOCharMap[i] for i in [0,1,3,4,5,6]))
    sortedStringToNumMap[six] = 6
    seven = tuple(sorted(posTOCharMap[i] for i in [0,2,5]))
    sortedStringToNumMap[seven] = 7
    eight = tuple(sorted(posTOCharMap[i] for i in [0,1,2,3,4,5,6]))
    sortedStringToNumMap[eight] = 8
    nine = tuple(sorted(posTOCharMap[i] for i in [0,1,2,3,5,6]))
    sortedStringToNumMap[nine] = 9
    return sortedStringToNumMap


def solution2(data):
    total = 0
    for line in data:
        inp, outp = line.split('|')
        inpCombinations = inp.split()
        for comb in inpCombinations:
            numUniqueChars = len(set(comb))
            if numUniqueChars == 2:
                numToStringMap[1] = comb
            elif numUniqueChars == 4:
                numToStringMap[4] = comb
            elif numUniqueChars == 3:
                numToStringMap[7] = comb
            elif numUniqueChars == 7:
                numToStringMap[8] = comb

        # find a
        for v in set(numToStringMap[7]) - set(numToStringMap[1]):
            posTOCharMap[0] = v


        # find 9
        for comb in inpCombinations:
            numUniqueChars = len(set(comb)) 
            if numUniqueChars == 6 and all(c in comb for c in numToStringMap[7]):
                numToStringMap[9] = comb
                break

        # find e
        for v in set(numToStringMap[8]) - set(numToStringMap[9]):
            posTOCharMap[4] = v

        # find g 
        for v in set(numToStringMap[8]) - set(numToStringMap[1]) - set(numToStringMap[4]) - set(numToStringMap[7]):
            if v not in posTOCharMap:
                posTOCharMap[6] = v

        # find f
        mostFreqChar = Counter(''.join(inpCombinations)).most_common()[0][0]
        posTOCharMap[5] = mostFreqChar
        for comb in inpCombinations:
            if mostFreqChar not in comb: # 2 found
                numToStringMap[2] = comb

        # find c
        oneString = numToStringMap[1]
        for c in oneString:
            if c not in posTOCharMap:
                posTOCharMap[2] = c
        
        # find d 
        for c in numToStringMap[2]:
            if c not in posTOCharMap:
                posTOCharMap[3] = c
        
        # find b
        for c in numToStringMap[8]:
            if c not in posTOCharMap:
                posTOCharMap[1] = c
        
        sortedStringToNumMap = createSortedStringToNumMap(posTOCharMap)
        outpCombinations = outp.split()
        n = 0
        for comb in outpCombinations:
            print(sortedStringToNumMap)
            n = 10 * n + sortedStringToNumMap[tuple(sorted(comb))]
        print(n)
        total += n
    return total

if __name__ == "__main__":
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, 'example.txt')) as file:
        data = file.read().splitlines()
        # print(solution(data))
        print(solution2(data))
