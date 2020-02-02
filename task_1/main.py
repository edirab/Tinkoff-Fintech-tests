

def main():
    monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = int(input())
    # while month > 12:
    #    month -= 12

    if month < 1 or month > 12:
        print("oh my god danila are you crazy")
    else:
        print(monthes[month-1])

    return


if __name__ == '__main__':
    main()
