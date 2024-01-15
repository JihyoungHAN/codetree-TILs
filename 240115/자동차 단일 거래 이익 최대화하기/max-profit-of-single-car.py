nYear = int(input())
arr = list(map(int, input().split()))

maxProfit = 0 

for i in range(nYear-1):
    for j in range(i+1, nYear):
        if arr[i] < arr[j] and (arr[j]-arr[i]) > maxProfit: 
            maxProfit = arr[j]-arr[i]

print(maxProfit)