stringA = input()
arr = []
letter = stringA[0]
arr.append(letter)
cnt = 1
strCnt = 2

for i in range(1, len(stringA)):
    if letter == stringA[i]:   
        cnt += 1
    else:
        letter = stringA[i]
        arr.append(cnt)
        arr.append(letter)
        cnt = 1
        strCnt += 2

arr.append(cnt)
print(strCnt)
for i in arr:
    print(i, end="")