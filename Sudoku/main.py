from util import print_question, find_zero, check_number
sample = [[1, 0, 0, 0, 7, 9, 0, 8, 0],
            [5, 9, 0, 0, 0, 2, 7, 3, 4],
            [7, 0, 0, 5, 3, 8, 0, 0, 9],
            [0, 0, 0, 3, 4, 0, 0, 2, 0],
            [3, 4, 0, 7, 2, 0, 0, 5, 1],
            [0, 5, 0, 8, 0, 0, 0, 0, 3],
            [0, 0, 7, 9, 0, 3, 5, 0, 8],
            [9, 1, 0, 0, 0, 0, 3, 0, 0],
            [6, 0, 0, 0, 0, 0, 1, 9, 0]]
# very difficult example
sample2 = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]


def solve(question):
    target = find_zero(question)
    if not target:
        return True
    else:
        target_row, target_col = target

        for num in range(1, 10):
            # backtracking key point
            if check_number(question, num, target):
                question[target_row][target_col] = num
                # print_question(question)
                # print('='*50)

                if solve(question):
                    # print_question(question)
                    return True

                question[target_row][target_col] = 0

    return False

print_question(sample2)
solve(sample2)
print('='*50)
print_question(sample2)