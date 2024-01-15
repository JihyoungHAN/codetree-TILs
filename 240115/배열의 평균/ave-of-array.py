arr = [list(map(int, input().split())) for _ in range(2)]

# horizontal average
for i in range(2):
    print(sum(arr[i])/4, end=" ")
print("")

# vertical average 
sumVal = 0
for i in range(4):
    for j in range(2):
        sumVal += arr[j][i]
    print(sumVal/2, end=" ")
    sumVal= 0
print("")

# whole average 
print((sum(arr[0])+sum(arr[1]))/8)