num = int(input())
value = 0
arr = [[0 for _ in range(num)] for _ in range(num)]

for i in range(num):
    for j in range(num): 
        value += 1
        arr[i][j] = value

for i in range(num):
    for j in range(num):
        print(arr[j][i], end=" ")
    print("")