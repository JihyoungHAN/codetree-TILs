numA, numB = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

check = "No"

for i in range(numA):
    if arrB[0] == arrA[i]:
        for j in range(numB):
            if arrB[j] == arrA[i+j]:
                check = "Yes"
            else:
                check = "No"
                break

print(check)