wordLenArr = [0 for _ in range(3)]
for i in range(3):
    wordLenArr[i] = len(input())

print(max(wordLenArr) - min(wordLenArr))