arr = list(map(int, input().split()))

maxVal = 0
minVal = 1001 

for i in arr:
    if i < 500 and i > maxVal:
        maxVal = i
    elif i > 500 and i < minVal:
        minVal = i

print(maxVal, minVal)