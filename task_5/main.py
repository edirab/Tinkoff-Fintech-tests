import copy

ways = 0
final_coords = []


class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def __str__(self):
        string = str(self.x) + " " + str(self.y)
        return string

    def copy(self):
        return copy.deepcopy(self)


def reached_position(current_point):

    if current_point.y == 8:
        global ways, final_coords
        ways += 1
        final_coords.append([current_point.x, current_point.y])
        return True
    else:
        return False


def step_left(current_point):
    if current_point.x > 1 and current_point.y < 8:
        current_point.x -= 1
        current_point.y += 1
    return


def step_right(current_point):
    if current_point.x < 8 and current_point.y < 8:
        current_point.x += 1
        current_point.y += 1
    return


def consider_all_ways(point):

    if reached_position(point):
        return

    point_copy = point.copy()

    if point.x > 1:
        step_left(point_copy)
        consider_all_ways(point_copy)

    point_copy = point.copy()

    if point.x < 8:
        step_right(point_copy)
        consider_all_ways(point_copy)
    return


def main():
    x, y = input().split()
    x = int(x)
    y = int(y)

    point = Point(x, y)

    steps_to_border = 8 - y

    if steps_to_border == 0:
        print(0)
        return

    consider_all_ways(point)
    print(ways)
    # print(final_coords)

    return


if __name__ == '__main__':
    main()
