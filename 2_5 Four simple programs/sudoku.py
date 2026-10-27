SUB_SET_RANGE = [
    [0, 3], [3, 6], [6, 9], # 2
]

# row check
def row_check(set):
    for row in set:
        for digit in row:
            if row.count(digit) != 1:
                return False
    return True

# column check
def column_check(set):
    for c_index in range(9):
        column = []
        for r_index in range(9):
            column.append(set[r_index][c_index])
        for digit in column:
            if column.count(digit) != 1:
                return False
    return True

# sub set check
def sub_set_check(set):
    for y_range in SUB_SET_RANGE:
        for x_range in SUB_SET_RANGE:
            sub_list = get_sub_set(set, x_range, y_range)
            for digit in sub_list:
                if sub_list.count(digit) != 1:
                    return False
    return True

# make set
def make_set():
    set = []
    row_cnt = 0
    print("Enter 9 digits of row:")
    while row_cnt != 9:
        row_in = input()
        if row_in.isnumeric() and len(row_in) == 9:
            set.append(row_in)
            row_cnt += 1
        else:
            print("invalid row entry")
    return set

# get sub set
def get_sub_set(set, x_range, y_range):
    # x_range   [#, #]
    # y_range   [#, #]
    # set       [##########],
    #           [##########],...
    sub_list = []
    for y in range(*y_range):
        for x in range(*x_range):
            sub_list.append(set[x][y])
    print(f'list length: {len(sub_list)}')
    return sub_list

if __name__ == "__main__":
    valid_set = True
    sudoku_set = make_set()
    valid_set = row_check(sudoku_set) and column_check(sudoku_set) and sub_set_check(sudoku_set)
    if valid_set:
        print("Valid")
    else:
        print("Invalid")

    # make code shorter with range( x, y, sub)?