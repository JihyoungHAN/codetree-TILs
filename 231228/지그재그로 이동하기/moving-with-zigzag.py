A, B = map(int, input().split())

num = 1
time = 1
distance = 0
result = 0
preResult = A
while result < B:
    if time%2 == 1:  
        result = A + num
    else:            
        result = A - num
    num *= 2
    distance += abs(preResult - result)
    if result > B: 
        distance -= (result - B)
    preResult = result
    time += 1
    

print(distance)