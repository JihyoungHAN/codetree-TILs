arr = list(map(int, input().split()))

evenArr = arr[1::2]
evenSum = sum(evenArr)

thirdArr = arr[2::3]
thirdAve = round(sum(thirdArr)/len(thirdArr), 1)

print(evenSum, thirdAve)