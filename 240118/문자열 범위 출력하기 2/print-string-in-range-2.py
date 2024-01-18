string = input()
n = int(input())
lenght = len(string)

for i in range(lenght-1, lenght-n-1, -1):
    if string[i] != " ":
        print(string[i], end="")

if string[0] != " ":
    print(string[lenght-n-1])