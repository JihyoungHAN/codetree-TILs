row, col = map(int, input().split())
arr_1 = [0 for _ in range(row)]
arr_2 = [0 for _ in range(row)]

for i in range(row):
    arr_1[i] = list(map(int, input().split()))
for i in range(row):
    arr_2[i] = list(map(int, input().split()))

for i in range(row): 
    for j in range(col):
        if arr_1[i][j] == arr_2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print("")