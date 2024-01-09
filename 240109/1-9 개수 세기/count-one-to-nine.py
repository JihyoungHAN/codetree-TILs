num = int(input())
arr = list(map(int, input().split()))
cntArr = [0] * 10

for i in arr:
    cntArr[i] += 1

for i in range(1, 10):
    print(cntArr[i])