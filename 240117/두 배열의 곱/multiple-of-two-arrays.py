arr_1 = [0 for _ in range(3)]
arr_2 = [0 for _ in range(3)]

for i in range(3):
    arr_1[i] = list(map(int, input().split()))
input()
for i in range(3):
    arr_2[i] = list(map(int, input().split()))

for i in range(3):
    print(arr_1[i][0]*arr_2[i][0], arr_1[i][1]*arr_2[i][1], arr_1[i][2]*arr_2[i][2])