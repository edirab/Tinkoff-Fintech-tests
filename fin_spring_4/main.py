
total_solutions = 0
valid_sequences = []


def check_sequence(brackets):
    result = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            result += 1
        elif brackets[i] == ')':
            result -= 1

            if result < 0:
                return result

    if result == 0:
        global total_solutions
        global valid_sequences
        total_solutions += 1
        valid_sequences.append(brackets.copy())

    return result


def resolve_question_marks(brackets):
    if len(brackets) % 2 == 1:
        return

    if '?' not in brackets:
        check_sequence(brackets)
        return

    brackets_copy = brackets.copy()

    for j in range(len(brackets)):
        if brackets[j] == '?':
            brackets_copy[j] = '('
            resolve_question_marks(brackets_copy)
            brackets_copy[j] = ')'
            resolve_question_marks(brackets_copy)
            return
    return


def print_valid_sequences(sequences):
    for i in range(len(sequences)):
        example = ""
        for j in range(len(sequences[i])):
            example += str(sequences[i][j])
            example += " "
        print(example)
    return


def main():
    string = input()
    bracket_list = list(string)
    # print(bracket_list)
    resolve_question_marks(bracket_list)
    print(total_solutions)
    # print_valid_sequences(valid_sequences)


if __name__ == '__main__':
    main()
