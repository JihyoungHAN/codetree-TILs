n = int(input())
length = 0 
cntA = 0

for i in range(n):
    string = input()
    length += len(string)
    if string[0] == "a":
        cntA += 1

print(length, cntA)