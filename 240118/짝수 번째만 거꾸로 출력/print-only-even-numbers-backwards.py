string = input()
evenStr = ""

for i in range(1, len(string), 2):
    evenStr += string[i]

for j in range(len(evenStr)-1, -1, -1):
    print(evenStr[j], end="")