import math 

n = int(input())
strArr = [input() for _ in range(n)]
letter = input()

cnt = 0 
length = 0 

for i in range(n):
    if strArr[i][0] == letter:
        cnt += 1
        length += len(strArr[i])

print(f"{cnt} {round(length/cnt, 2):.2f}")