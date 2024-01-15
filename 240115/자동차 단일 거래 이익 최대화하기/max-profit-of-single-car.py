nYear = int(input())
arr = list(map(int, input().split()))

maxProfit = 0 

for i in range(nYear-1):
    for j in range(i+1, nYear):
        if i < j and (j-i) > maxProfit: 
            maxProfit = j-i

print(maxProfit)