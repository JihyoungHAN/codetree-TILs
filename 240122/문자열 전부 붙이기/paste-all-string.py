n = int(input())
arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = input()

print("".join(arr))