strArr = tuple(input().split())
length = 0 

for i in range(10):
    length += len(strArr[i])

print(length)