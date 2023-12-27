arr = list(map(int, input().split()))

for i in range(0, len(arr)):
    if arr[i] == 0:
        print(arr[i-1] + arr[i-2] + arr[i-3])
        break;