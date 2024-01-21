n = int(input())
arr = list(input().split())
allString = "".join(arr)
cnt = 0

for i in range(len(allString)):
    if cnt < 5: 
        print(allString[i], end="")
        cnt += 1
    else:
        print()
        print(allString[i], end="")
        cnt = 1