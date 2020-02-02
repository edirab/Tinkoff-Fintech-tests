
current_x = minDist = 100

N = input()
# print(N)

for i in range(int(N)):
    data = int(input())
    current_x += data

    if abs(current_x) < minDist:
        minDist = abs(current_x)
    # print(data)
print(minDist)

