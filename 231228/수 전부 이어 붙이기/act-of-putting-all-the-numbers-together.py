num = int(input())
numArr = list(input().split())

allNum = ""

for i in range(num):
    allNum += numArr[i]

fiveNum = ""
for i in range(len(allNum)):
    if len(fiveNum) < 5: 
        fiveNum += allNum[i]
    else:
        print(fiveNum)
        fiveNum = allNum[i]

print(fiveNum)