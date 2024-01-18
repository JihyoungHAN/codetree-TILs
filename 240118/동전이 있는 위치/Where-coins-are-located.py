n, m = map(int, input().split())
coinArr = [list(map(int, input().split())) for _ in range(m)]
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in coinArr:
    arr[i[0]-1][i[1]-1] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()