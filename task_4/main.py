def multiply_by_S(S, i):
    return int(i) * S


def main():
    delays = 0

    N, S = input().split()
    N = int(N)
    S = int(S)

    velocities = [0] * N
    velocities = input().split()

    #print(velocities)

    for i in range(len(velocities)):
        velocities[i] = int(velocities[i]) * S

    print(velocities)
    j = k = 0

    while k < len(velocities):
        if velocities[j] > velocities[k]:
            delays += 1
            k += 1
        else:
            j = k
            k += 1

    print(delays)
    return


if __name__ == '__main__':
    main()
