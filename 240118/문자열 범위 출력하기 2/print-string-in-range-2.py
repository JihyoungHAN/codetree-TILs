string = input()
n = int(input())
lenght = len(string)

for i in range(lenght-1, lenght-n-2, -1):
    if string[i] != " ":
        print(string[i], end="")