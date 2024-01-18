strArr = ["apple", "banana", "grape", "blueberry", "orange"]
letter = input()
cnt = 0

for i in strArr:
    if i[2] == letter or i[3] == letter:
        print(i)
        cnt += 1

print(cnt)