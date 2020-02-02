
def get_coords(coords_list, lengths_list):
    for i in range(len(lengths_list)):
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        coords_list.append([a, b])
        lengths_list[i] = (b-a+1)
    return


def fill_line(line_list, coords_list):
    for j in range(len(coords_list)):
        begin = coords_list[j][0]
        end = coords_list[j][1]

        print(begin, end)
        for k in range(begin, end+1):
            line_list[k - 1] = j + 1
    return


def main():
    total_messages = 0

    N = int(input())  # длина полоски
    M = int(input())  # количество измерений

    line = [0] * N
    coords = []
    lengths = [0] * M
    messages_left = [0] * M

    get_coords(coords, lengths)
    fill_line(line, coords)

    for i in range(len(line)):
        elem = line[i]
        if elem != 0:
            messages_left[elem - 1] += 1

    for j in range(len(lengths)):
        if messages_left[j] == lengths[j]:
            total_messages += 1

    print(line)
    print(coords)
    print(lengths)
    print(messages_left)

    print(total_messages)
    return


if __name__ == '__main__':
    main()
