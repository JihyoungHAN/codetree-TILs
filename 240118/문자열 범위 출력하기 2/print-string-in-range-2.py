string = input()
n = int(input())
if string[-1] == " ":
    string = string[:-1]
length = len(string)

if length < n:
    for i in range(length-1, -1, -1):
        print(string[i], end="")
else: 
    for i in range(length-1, length-n-1, -1):
        print(string[i], end="")