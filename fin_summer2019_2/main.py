
def encrypt():

    _2n = list()
    _2n_1 = list()

    for i in range(0, len(str_), 2):
        _2n_1.append(str_[i])

    for i in range(1, len(str_), 2):
        _2n.append(str_[i])

    print(str(_2n))
    print(str(_2n_1))

    str_encrypted_list = []

    j = k = 0

    for r in range(len(str_)):
        print("k, j = ")
        print(k, j)

        if k > j:

            str_encrypted_list.append(_2n_1[j])
            j += 1
        else:
            str_encrypted_list.append(_2n[k])
            k += 1

    print(str(str_encrypted_list))


def decrypt(str_):

    str_decrypted = ""
    _2n_list = list()
    _2n_1_list = list()
    str_decrypted_list = list()

    _2n = len(str_) // 2
    _2n_1 = len(str_) - _2n
    # print(_2n, _2n_1)

    for i in range(_2n):
        _2n_list.append(str_[i])
    for j in range(_2n, len(str_)):
        _2n_1_list.append(str_[j])

    # print(str(_2n_list))
    # print(str(_2n_1_list))

    for r in range(len(_2n_1_list)):
        str_decrypted_list.append(_2n_1_list[r])

        if r < len(_2n_list):
            str_decrypted_list.append(_2n_list[r])

    print(str_decrypted.join(str_decrypted_list))
    return


str_ = input()
print(len(str_))
decrypt(str_)






