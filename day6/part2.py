from collections import Counter, defaultdict
import copy
with open('data.txt') as f:
    for line in f.readlines():
        if not line:
            continue
        countdownCounter = Counter([int(n) for n in line.split(',')])
        for _ in range(256):
            newCounter = defaultdict(int)
            for i in range(9):
                if i == 0:
                    newCounter[8] += countdownCounter[0]
                    newCounter[6] += countdownCounter[0] 
                else:
                    newCounter[i - 1] += countdownCounter[i]
            countdownCounter = newCounter.copy()
        print(sum(countdownCounter.values()))
