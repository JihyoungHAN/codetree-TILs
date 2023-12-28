arr = list(map(int, input().split()))

oddAdd = arr[0] + arr[2] + arr[4] + arr[6] + arr[8] 
evenAdd = arr[1] + arr[3] + arr[5] + arr[7] + arr[9]

result = abs(oddAdd - evenAdd)
print(result)