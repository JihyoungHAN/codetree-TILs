word = ['L', 'E', 'B', 'R', 'O', 'S']
letter = input()

if letter not in word:
    print("None")
else: 
    print(word.index(letter))