f = open('data.txt', 'r') 
arr = []
for line in f.read().splitlines():
    arr.append(line)

binaryLen = 12

oneCounts = [0 for _ in range(binaryLen)]
oxygenRating = ""
co2Rating = ""

for num in arr:
    for i, c in enumerate(num):
        if c == '1':
            oneCounts[i] += 1

n = len(arr)

oxyNumber = "".join(['1' if oneCounts[idx] >= n / 2  else '0' for idx in range(len(oneCounts))] )
print(arr.count(oxyNumber))
co2Num = ["1" if n == "0" else "1" for n in oxyNumber]
print(arr.count(co2Num))

oxyList = arr[:]
idx = 0
while idx < len(oneCounts) and len(oxyList) > 1:
    mostFreqBit = '1' if oneCounts[idx] >= n / 2 else '0'
    oxyList = [s for s in oxyList if s[idx] == mostFreqBit]
    idx += 1

co2List = arr[:]
idx = 0
while idx < len(oneCounts) and len(co2List) > 1:
    # print(len(co2List))
    # print(co2List, idx)
    leastFreqBit = '1' if oneCounts[idx] < n / 2 else '0' 
    co2List = [s for s in co2List if s[idx] == leastFreqBit]
    idx += 1

print(oxyList, co2List)
# print(int(s,2)*int(s2,2))
# print(arr, n)








