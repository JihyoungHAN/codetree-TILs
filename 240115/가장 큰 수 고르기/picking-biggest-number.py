arr = list(map(int, input().split()))
maxVal = 0

for i in arr:
    if i > maxVal:
        maxVal = i

print(maxVal)