n, q = map(int, input().split())

questions = [0] * q
arr = list(map(int, input().split()))

for i in range(q):
    questions[i] = list(map(int, input().split()))

for  i in range(q):
    if questions[i][0] == 1:
        print(arr[questions[i][1] - 1])
    elif questions[i][0] == 2:
        if questions[i][1] in arr:
            print(arr.index(questions[i][1]) + 1)
        else: 
            print(0)
    elif questions[i][0] == 3: 
        for i in range(questions[i][1]-1, questions[i][2]):
            print(arr[i], end=" ")