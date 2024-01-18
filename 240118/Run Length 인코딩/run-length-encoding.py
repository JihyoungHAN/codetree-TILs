stringA = input()
arr = []
letter = stringA[0]
arr.append(letter)
cnt = 1

for i in range(1, len(stringA)):
    if letter == stringA[i]:   
        cnt += 1
    else:
        letter = stringA[i]
        arr.append(cnt)
        arr.append(letter)
        cnt = 1


arr.append(cnt)
print(len(arr))
for i in arr:
    print(i, end="")