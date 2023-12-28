num = int(input())
arr = list(map(int, input().split()))

evenArr = [arr[i] for i in range(num) if arr[i]%2 == 0]
for i in range(len(evenArr)):
    print(evenArr[i], end=' ')