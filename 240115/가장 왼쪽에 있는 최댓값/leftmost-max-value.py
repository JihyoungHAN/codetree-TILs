num = int(input())
arr = list(map(int, input().split()))

maxVal = 0
maxIndex = 0 

while True: 
    for i in range(num):
        if arr[i] > maxVal:
            maxVal = arr[i]
            maxIndex = i
    print(maxIndex+1, end=" ")
    num = maxIndex
    maxVal = 0
    if maxIndex == 0: 
        break