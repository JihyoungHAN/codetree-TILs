gradeArr = list(map(int, input().split()))
cntArr = [0] * 11

for i in gradeArr:
    if i == 0:
        break
    else:
        div = i // 10
        if div != 0:
            cntArr[div] += 1

for i in range(10, 0, -1):
    print(i*10, "-", cntArr[i])