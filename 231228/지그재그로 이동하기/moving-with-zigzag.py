A, B = map(int, input().split())

num = 1 #이동할 거리
time = 1 #더할지 뺄지 결정요소 
distance = 0 #전체 간 거리
result = A #B랑 비교할 값 

while result != B:
    if time%2 == 1: # 더하기 
        for i in range(abs(result-(A+num))):
            result += 1
            distance += 1
            if result == B: 
                break;       
    else:           # 빼기 
        for i in range(abs(result-(A-num))):
            result -= 1 
            distance += 1
            if result == B: 
                break; 
    num += 1
    time += 1 
    

print(distance)