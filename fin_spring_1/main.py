n = int(input())

palindromes_count = 0

for i in range(1, n + 1):
    if i == int(str(i)[::-1]):
        palindromes_count += 1

print(palindromes_count)
