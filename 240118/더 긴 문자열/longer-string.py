firstWord, secondWord = input().split()

if len(firstWord) > len(secondWord):
    print(firstWord, len(firstWord))
elif len(firstWord) < len(secondWord):
    print(secondWord, len(secondWord))
else:
    print("same")