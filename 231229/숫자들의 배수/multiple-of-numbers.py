num = int(input())
arr = []
time = 0
for i in range(10):
    arr.append(num*(i+1))
    if (num*(i+1))%5 == 0:
        time += 1
    if time == 2:
        break 
    
for i in range(len(arr)):
    print(arr[i], end=' ')