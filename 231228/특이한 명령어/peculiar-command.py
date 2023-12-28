num = int(input())
orders = [0 for i in range(num)]

for i in range(num):
    orders[i] = list(input().split())

for i in range(num): 
    if orders[i][2] == "s": 
        print(int(orders[i][0]) * int(orders[i][1]))
    if orders[i][2] == "t": 
        print(round(int(orders[i][0]) * int(orders[i][1]) * 1/2, 1))