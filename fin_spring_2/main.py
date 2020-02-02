string = input()

letters = [0]*27

for i in range(len(string)):
    # print(ord(string[i]) - ord('a'))
    letters[ord(string[i]) - ord('a')] += 1

# print(letters)

for j in range(len(letters)):
    if letters[j] != 0:
        print(chr(j + ord('a')), end='')


