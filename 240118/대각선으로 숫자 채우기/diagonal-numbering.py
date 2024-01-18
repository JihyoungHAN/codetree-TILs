n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(m+n-1):
    for j in range(i+1):
        row = j 
        col = i - j
        if row == n:
            break 
        if col <= m-1:
            arr[row][col] = num
            num += 1 
        else:
            continue
        

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()