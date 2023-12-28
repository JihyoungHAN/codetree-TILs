num = int(input())
arr = list(map(int, input().split()))\

doublArr = [i**2 for i in arr]
for i in range(len(doublArr)):
    print(doublArr[i], end=' ')