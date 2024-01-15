import sys

num = int(input())
arr = list(map(int, input().split()))
minVal = sys.maxsize
cnt = 0;

for i in arr:
    if i < minVal:
        minVal = i
        cnt = 1
    elif i == minVal: 
        cnt += 1

print(minVal, cnt)