n, m = map(int, input().split())
arr = list(map(int, input().split()))
order = [[0, 0, 0] for i in range(m)]

for i in range(m):
    order[i][0], order[i][1], order[i][2] = map(int, input().split())

for i in range(m):
    a = order[i][0]
    b = order[i][1]
    c = order[i][2]
    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            if arr[j] == 0:
                arr[j] = 1
            elif arr[j] == 1:
                arr[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            arr[j] = 0
    elif a == 4:
        for j in range(b-1, c):
            arr[j] = 1

for i in range(n):
    print(arr[i], end=" ")