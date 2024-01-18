string = input()
smallLetter = input()
cnt = 0

for i in range(len(string)):
    if string[i] == smallLetter:
        cnt += 1

print(cnt)