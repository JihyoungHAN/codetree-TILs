wordArr = [0 for i in range(5)]
lenArr = [0 for i in range(5)]
for i in range(5):
    wordArr[i] = input()
    lenArr[i] = len(wordArr[i])

result = ""

for i in range(5): 
    for j in range(5):
        if lenArr[j] != 0:
            result += wordArr[j][i]
            lenArr[j] -= 1 

print(result)