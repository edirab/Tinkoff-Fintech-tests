import main
import random


N = random.randint(4, 10)
points = [0] * N
segments = [0] * N

# генерируем точки
for i in range(N):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    points[i] = [x, y]


# генерируем отрезки
for i in range(len(points)):
    segments[i] = [points[-1+i], points[i]]


for j in range(len(segments)):
    string = "(" + str(segments[j][0][0]) + ", " + str(segments[j][0][1]) + ") (" + str(segments[j][1][0]) + ", " + str(segments[j][1][1]) + ")"
    print(string)

for j in range(len(segments)):
    k, b = main.line_equation(segments[j][0][0], segments[j][0][1], segments[j][1][0], segments[j][1][1])
    string = str(j+1) + ". y = " + str(k) + " * x + " + str(b)
    print(string)
