a, b = map(int, input().split())
cntArr = [0] * b 

while True:
    div = a // b
    rem = a % b 
    cntArr[rem] += 1
    a = div
    if div == 0: 
        break 

result = 0
for i in cntArr:
    result += i ** 2

print(result)