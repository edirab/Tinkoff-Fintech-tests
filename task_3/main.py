import re


def main():
    passwd = input()

    if len(passwd) < 8:
        print("NO")
        return

    elif re.search('[\\\[\]{ }|@<>#$%^&+=\\-*()?!.,;~_"\'/]', passwd):
        print("NO")
        return

    elif re.search('[A-Z]', passwd) == False:
        print("NO")
        return

    elif re.search('[a-z]', passwd) == False:
        print("NO")
        return

    elif re.search('[0-9]', passwd) == False:
        print("NO")
        return

    else:
        print("YES")
    return


if __name__ == '__main__':
    main()
