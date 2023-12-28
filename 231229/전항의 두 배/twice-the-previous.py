first, second = map(int, input().split())

print(first, second, end=" ")

for _ in range(8):
    print(second + first * 2, end=" ")
    eff = second
    second = first*2 + second 
    first = eff