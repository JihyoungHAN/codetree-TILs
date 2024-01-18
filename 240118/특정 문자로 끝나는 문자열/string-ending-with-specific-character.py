strArr = [input() for _ in range(10)]
letter = input()
cnt = 0 

for i in range(10):
    if strArr[i][-1] == letter:
        print(strArr[i])
        cnt += 1

if cnt == 0:
    print("None")