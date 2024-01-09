arr = [0] * 3
symArr = [0] * 4 # 0 - A / 1 - B / 2 - C / 3 - D
for i in range(3):
    arr[i] = list(input().split())

for i in range(3):
    if arr[i][0] == "Y":
        if int(arr[i][1]) >= 37:
            symArr[0] += 1 
        else: 
            symArr[2] += 1
    else: #"N"
        if int(arr[i][1]) >= 37: 
            symArr[1] += 1
        else:
            symArr[3] += 1 

if symArr[0] >= 2:
    print(symArr[0], symArr[1], symArr[2], symArr[3], "E")
else:
    print(symArr[0], symArr[1], symArr[2], symArr[3])