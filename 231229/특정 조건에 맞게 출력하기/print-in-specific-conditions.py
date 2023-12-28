arr = list(map(int, input().split()))
newArr = []
for i in range(len(arr)):
    if arr[i] == 0:
        break
    elif arr[i]%2 == 1:
        newArr.append(arr[i]+3)
    else:
        newArr.append(arr[i]//2)

for i in range(len(newArr)):
    print(newArr[i], end=' ')