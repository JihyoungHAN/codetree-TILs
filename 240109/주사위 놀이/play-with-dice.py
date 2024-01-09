diceNumArr = list(map(int, input().split()))
cntArr = [0] * 7

for i in diceNumArr:
    cntArr[i] += 1

for i in range(1, 7):
    print(i, "-", cntArr[i])