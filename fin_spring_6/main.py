intersections = 0


class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def __str__(self):
        string = str(self.x) + " " + str(self.y)
        return string


def get_polygon_points(N, points_list):

    for i in range(N):
        a, b = input().split()
        a = int(a)
        b = int(b)
        points_list[i] = Point(a, b)
    return


def line_equation(ax, ay, bx, by):
    '''
    b = (x1 * y2 - x2 8 y1) / (x1 - x2)
    k = (y1 - b)/x1 = (y2-b)/x2
    '''
    b = ax * by - bx * ay
    b = b / (ax - bx)

    k = 0
    if ax != 0:
        k = (ay - b) / ax
    else:
        k = (by - b) / bx
    return k, b


def check(location_point, points_list):
    segments = []
    global intersections

    for i in range(len(points_list)):
        segments.append([points_list[-1+i], points_list[i]])

    for j in range(len(segments)):
        string = "(" + str(segments[j][0].x) + ", " + str(segments[j][0].y) + ") (" + str(segments[j][1].x) + ", " + str(segments[j][1].y) + ")"
        # print(string)

    for k in range(len(segments)):
        # print(type(k))
        # print(type(segments[k]))
        # print(type(segments[k][0]))

        ax = segments[k][0].x - location_point.x
        ay = segments[k][0].y - location_point.y
        bx = segments[k][1].x - location_point.x
        by = segments[k][1].y - location_point.y

        # по одну сторону от прямой
        if ay * by > 0:
            continue

        # ур-ие вида x = const
        if ax == bx:
            if ax > 0:
                intersections += 1
            continue

        # kx + b = 0 -> x = -b/k
        else:
            k, b = line_equation(ax, ay, bx, by)
            x = -b/k
            # print("x: ", x)
            if x > 0:
                intersections += 1

    return


def main():
    N = int(input())
    points = [None] * N
    get_polygon_points(N, points)

    x, y = input().split()
    x = float(x)
    y = float(y)
    location = Point(x, y)

    check(location, points)
    # print("intersections: ", intersections)

    if intersections % 2:
        print("YES")
    else:
        print("NO")

    # print(str(points))
    # print(location)

    return


if __name__ == '__main__':
    main()
