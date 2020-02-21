sample = [[1, 0, 0, 0, 7, 9, 0, 8, 0],

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

# print_question(question)

def find_zero(question):
    for row in range(len(question[0])):
        for col in range(len(question[1])):
            if question[row][col] == 0:
                return (row, col)

    return None


def check_number(question, num, postion:tuple):
    # check row cannot duplicate
    for idx in range(len(question[0])): # len(question[0]) = 1
        if question[postion[0]][idx] == num and postion[1] != idx: # if number have already in input_row return False
            return False

    # check column cannot duplicate
    for idx in range(len(question[0])):
        if question[idx][postion[1]] == num and postion[0] != idx: # if number have already in input_col return False
            return False

    # check cube 1 to 9
    cube_xaxis = postion[1] // 3 # return which position in big 9 square
    cube_yaxis = postion[0] // 3

    for row in range(cube_yaxis*3, cube_yaxis*3 + 3): # y_index check row
        for col in range(cube_xaxis*3, cube_xaxis*3 + 3): # x_index check columns
            if question[row][col] == num and (row, col) != postion:
                return False

    return True


