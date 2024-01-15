num = int(input())
arr = list(map(int, input().split()))

maxVal = 0 
isDup = 0 

while True:
    for i in range(num):
        if arr[i] > maxVal:
            maxVal = arr[i] 
            isDup = 0 
        elif arr[i] == maxVal: 
            for j in range(num):
                if arr[j] == maxVal:
                    arr[j] = -1 
            maxVal = 0 
            isDup = 1
            break
    if isDup == 0 and maxVal != 0:
        print(maxVal)
        break
    elif isDup == 1 and maxVal == 0:
        print(-1)
        break