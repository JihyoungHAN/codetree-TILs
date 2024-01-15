num = int(input())
arr = list(map(int, input().split()))

minVal = 100

for i in range(num):
    for j in range(num):
        if i > j and (arr[i]-arr[j]) < minVal:
            minVal = arr[i] - arr[j]
        if j > i and (arr[j]-arr[i]) < minVal:
             minVal = arr[j] - arr[i]
    
print(minVal)