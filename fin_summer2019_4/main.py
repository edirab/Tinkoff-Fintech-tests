import copy


class Rect:
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def __str__(self):
        string = "(" + str(self.x1) + ", " + str(self.y1) + ") " + \
                 "(" + str(self.x2) + ", " + str(self.y2) + ")"
        return string


rects = []

n, m = input().split(' ')
n = int(n)
m = int(m)

arr = []
for _ in range(n):
    row = input().split(' ')
    arr.append([int(item) for item in row])

print(arr)


for i in range(n):
    k = 0
    r = Rect(0, 0)

    for j in range(m):
        # print(i, " ", j)
        if arr[i][j] == 0:
            k += 1
            print(i, " ", j)
            # если первая белая клетка
            if k == 1:
                r.x1, r.y1 = j, i

        else:
            if k != 0:
                r.x2, r.y2 = r.x1 + k - 1, i
                rects.append(copy.deepcopy(r))
                k = 0

    if k != 0:
        r.x2, r.y2 = r.x1 + k - 1, i
        rects.append(r)


for r in rects:
    print(str(r))
