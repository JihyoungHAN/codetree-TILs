arr = [0 for i in range(10)]
arr[0], arr[1] = map(int, input().split())

for i in range(2, len(arr)):
    sumVal= arr[i-1] + arr[i-2]
    arr[i] = sumVal%10

for i in arr:
    print(i, end=' ')