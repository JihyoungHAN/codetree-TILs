import sys
arr = list(map(int, input().split()))

maxVal = -sys.maxsize
minVal = sys.maxsize

for i in arr:
    if i == 999 or i == -999:
        break
    if i > maxVal:
        maxVal = i
    if i < minVal: 
        minVal = i
    

print(maxVal, minVal)