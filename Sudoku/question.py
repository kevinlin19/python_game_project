question = [[1, 0, 0, 0, 7, 9, 0, 8, 0],

            [5, 9, 0, 0, 0, 2, 7, 3, 4],
            [7, 0, 0, 5, 3, 8, 0, 0, 9],
            [0, 0, 0, 3, 4, 0, 0, 2, 0],
            [3, 4, 0, 7, 2, 0, 0, 5, 1],
            [0, 5, 0, 8, 0, 0, 0, 0, 3],
            [0, 0, 7, 9, 0, 3, 5, 0, 8],
            [9, 1, 0, 0, 0, 0, 3, 0, 0],
            [6, 0, 0, 0, 0, 0, 1, 9, 0]]

def print_question(question):
    '''
    parameters:
        question (list): size 9*9 sudoku question

    return:
        print string

    example:
    >>>print_question(question)
    －－－－－－－－－－－－－
    | 1 0 0 | 0 7 9 | 0 8 0 |
    | 5 9 0 | 0 0 2 | 7 3 4 |
    | 7 0 0 | 5 3 8 | 0 0 9 |
    －－－－－－－－－－－－－
    | 0 0 0 | 3 4 0 | 0 2 0 |
    | 3 4 0 | 7 2 0 | 0 5 1 |
    | 0 5 0 | 8 0 0 | 0 0 3 |
    －－－－－－－－－－－－－
    | 0 0 7 | 9 0 3 | 5 0 8 |
    | 9 1 0 | 0 0 0 | 3 0 0 |
    | 6 0 0 | 0 0 0 | 1 9 0 |
    －－－－－－－－－－－－－
    '''

    for r_idx, row in enumerate(question):
        if (r_idx % 3 == 0):
            print('－'*13)

        for c_idx, col in enumerate(row):
            if (c_idx % 3 == 0) and (c_idx != 8):
                print('|', end =" ")
            print(col, end=" ")

            if c_idx == 8:
                print('|')

        if r_idx == 8:
            print('－'*13)

print_question(question)