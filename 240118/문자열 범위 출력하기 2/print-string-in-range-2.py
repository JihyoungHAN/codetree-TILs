string = input()
n = int(input())
if string[-1] == " ":
    string = string[:-1]
length = len(string)

if length < n:
    print(string)
else: 
    for i in range(length-1, length-n-1, -1):
        print(string[i], end="")