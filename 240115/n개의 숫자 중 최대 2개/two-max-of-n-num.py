num = int(input())
arr = list(map(int, input().split()))


for i in range(1,num):
    if arr[i] < arr[i-1]:
        for j in range(i-1,-1,-1):
            if arr[j+1] > arr[j]:
                break
            leave = arr[j+1]
            arr[j+1] = arr[j] 
            arr[j] = leave

print(arr[num-1], arr[num-2])