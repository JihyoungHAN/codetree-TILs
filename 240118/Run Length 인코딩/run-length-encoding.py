stringA = input()
result = ""
letter = stringA[0]
result += letter
cnt = 1

for i in range(1, len(stringA)):
    if letter == stringA[i]:   
        cnt += 1
    else:
        letter = stringA[i]
        result += str(cnt)
        result += letter
        cnt = 1


result += str(cnt)
print(len(result))
print(result)