'''
old fish - create new fish every 7 days
new fish - create new fish 9 days followed by 7


3,4,3,1,2
2,3,2,0,1
1,2,1,6,0,8
0,1,0,5,6,7,8
'''


with open('data.txt') as f:
    for line in f.readlines():
        if not line:
            continue
        countdownArr = [int(n) for n in line.split(',')]
        for _ in range(256):
            newFish = []
            for i, daysLeft in enumerate(countdownArr):
                if daysLeft == 0:
                    countdownArr[i] = 6
                    newFish.append(8)
                else:
                    countdownArr[i] -= 1
            countdownArr += newFish
        print(len(countdownArr))