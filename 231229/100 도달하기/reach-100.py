num = int(input())
first = 1 
second = num

print(first, second, end=" ")

while True:  
    print(first + second, end=" ")
    default = second
    second = first + second 
    first = default 
    if first+second > 100:
        print(first + second, end=" ")
        break