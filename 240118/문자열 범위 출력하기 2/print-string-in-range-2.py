string = input()
n = int(input())
if string[-1] == " ":
    string = string[:-1]
lenght = len(string)


for i in range(lenght-1, lenght-n-1, -1):
    print(string[i], end="")