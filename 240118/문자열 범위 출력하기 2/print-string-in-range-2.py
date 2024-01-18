string = input()
n = int(input())
lenght = len(string)

for i in range(lenght-2, lenght-n-2, -1):
    print(string[i], end="")