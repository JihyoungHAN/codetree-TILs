arr = list(map(int, input().split()))
tenArr = [0] * 10 

for i in arr:
    if i == 0:
        break
    else:
        div = i // 10 
        if div != 0:
            tenArr[div] += 1

for i in range(1, 10):
    print(i, "-", tenArr[i])