
def extract_coeffs(polynom):
    polynom_elems_list = polynom.replace('-', '+-').replace('^', '').split('+')
    # print(polynom_elems_list)

    polynom_coeffs = {}
    for item in polynom_elems_list:
        coeffs_list = item.split('x')
        # print(coeffs_list)

        if coeffs_list[0] == '':
            coeffs_list[0] = 1
        elif coeffs_list[0] == '-':
            coeffs_list[0] = -1
        else:
            coeffs_list[0] = int(coeffs_list[0])

        # case '1' для свободного члена
        if len(coeffs_list) == 1:
            polynom_coeffs[0] = int(coeffs_list[0])
        # case 'x' -> ['', ''] если степень отсутсвует, то есть первая
        elif coeffs_list[1] == '':
            polynom_coeffs[1] = coeffs_list[0]
        else:
            polynom_coeffs[int(coeffs_list[1])] = coeffs_list[0]

    print(polynom_coeffs)
    return (polynom_coeffs)


def multiplicate_polynoms(p1, p2):
    polynoms_to_sum = []
    for p1_key in p1.keys():
        intermediate_polynom_dict = {}
        for p2_key in p2.keys():
            intermediate_polynom_dict[p1_key + p2_key] = p1[p1_key] * p2[p2_key]
        polynoms_to_sum.append(intermediate_polynom_dict)

    print(polynoms_to_sum)

    # приводим подобные
    result_dict = {}
    for dictionary in polynoms_to_sum:
        for key in dictionary.keys():
            if key in result_dict:
                result_dict[key] += dictionary[key]
            else:
                result_dict[key] = dictionary[key]

    print(result_dict)
    return (result_dict)


def print_result(result_dict):
    result_string = ''
    for key in sorted(result_dict, reverse=True):
        if result_dict[key] != 0:
            if result_dict[key] > 0 and result_string != '':
                result_string += '+'
            if result_dict[key] < 0:
                result_string += '-'
                result_dict[key] *= -1
            if result_dict[key] != 1 or key == 0:
                result_string += str(result_dict[key])
            if key > 1:
                result_string += 'x^'
                result_string += str(key)
            elif key == 1:
                result_string += 'x'

    if result_string == '':
        print(0)
    else:
        print(result_string)


def main():
    first_polynom = input()
    second_polynom = input()
    p1_coeffs = extract_coeffs(first_polynom)
    p2_coeffs = extract_coeffs(second_polynom)
    result_polynom_dict = multiplicate_polynoms(p1_coeffs, p2_coeffs)
    print_result(result_polynom_dict)

if __name__ == '__main__':
    main()