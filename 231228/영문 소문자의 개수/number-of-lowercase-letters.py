num = int(input())
arr = list(input().split())

smallNum = 0
for i in range(num):
    if arr[i].isalpha() & arr[i].islower():
        smallNum += 1
    else:
        break

alphabet = {} 
for i in range(smallNum):
    if arr[i] in alphabet:
        alphabet[arr[i]] += 1; 
    else: 
        alphabet[arr[i]] = 1; 


keyArr = sorted(list(alphabet.keys()))
for k in keyArr:
    print(k, ":", alphabet[k])