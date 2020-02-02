
def main():
    seats = []
    a, b = input().split()
    a = int(a)
    b = int(b)

    for i in range(a, b+1):
        square = i * i
        # n = len(str(i))
        str_square = str(square)

        if str_square.endswith(str(i)):
            seats.append(i)

    if len(seats) == 0:
        print(-1)
    else:
        for j in range(len(seats)):
            print(seats[j], end=' ')

    return


if __name__ == '__main__':
    main()
