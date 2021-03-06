def is_move_valid(arr, i, j):
    return 0 <= i < len(arr) and 0 <= j < len(arr[i])


def find_current_longest_adjacent_sequence(arr, i, j):
    if not is_move_valid(arr, i, j):
        return None

    # when go back to older cells it may find neighbour that is lowercase too, so we make sure it wont count it again
    # by returning 0

    if arr[i][j] == 'r' or arr[i][j] == 'g' or arr[i][j] == 'b':
        return 0
    current_count = 0

    # move up
    if i - 1 >= 0 and arr[i - 1][j] == arr[i][j]:
        # turns previous cell into a lower case so the programs knows which cell has been visited and it doesn't
        # loop endlessly
        arr[i][j] = arr[i][j].lower()
        current_count += find_current_longest_adjacent_sequence(arr, i - 1, j)

    # move left
    if j - 1 >= 0 and arr[i][j - 1] == arr[i][j]:
        arr[i][j] = arr[i][j].lower()
        current_count += find_current_longest_adjacent_sequence(arr, i, j - 1)

    # move right
    if j + 1 < len(arr[i]) and arr[i][j + 1] == arr[i][j]:
        arr[i][j] = arr[i][j].lower()
        current_count += find_current_longest_adjacent_sequence(arr, i, j + 1)

    # move down
    if i + 1 < len(arr) and arr[i + 1][j] == arr[i][j]:
        arr[i][j] = arr[i][j].lower()
        current_count += find_current_longest_adjacent_sequence(arr, i + 1, j)

    # at the end turns the cell back to normal because it has to go back to older cells and check for more matching
    # neighbour cells
    arr[i][j] = arr[i][j].upper()
    if current_count > 0:
        return current_count + 1
    else:
        return 1


def find_longest_adjacent_sequence(arr):
    current_len = 0
    max_len = 0

    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            current_len = find_current_longest_adjacent_sequence(arr, i, j)
            if current_len > max_len:
                max_len = current_len
    return max_len


def main():
    # input_arr = [
    #     ['R', 'R', 'R', 'G'],
    #     ['G', 'B', 'R', 'G'],
    #     ['R', 'G', 'G', 'G'],
    #     ['G', 'G', 'B', 'B']
    # ]

    # input_arr = [
    #     ['R', 'R', 'R', 'G'],
    #     ['G', 'B', 'R', 'G'],
    #     ['R', 'G', 'G', 'G'],
    #     ['G', 'G', 'B', 'B']
    # ]

    # input_arr = [
    #     ['R', 'R', 'R', 'R'],
    #     ['R', 'R', 'R', 'R'],
    #     ['R', 'R', 'R', 'R'],
    #     ['R', 'R', 'R', 'R'],
    #     ['R', 'R', 'R', 'R'],
    #     ['R', 'R', 'R', 'R'],
    # ]

    input_arr = [
        ['R', 'R', 'B', 'B', 'B', 'B'],
        ['B', 'R', 'B', 'B', 'G', 'B'],
        ['B', 'G', 'G', 'B', 'R', 'B'],
        ['B', 'B', 'R', 'B', 'G', 'B'],
        ['R', 'B', 'R', 'B', 'R', 'B'],
        ['R', 'B', 'B', 'B', 'G', 'B'],
    ]

    # user_input = input()
    # matrix_size = user_input.split()
    # rows = int(matrix_size[0])
    # cols = int(matrix_size[1])
    # input_arr = []
    # for i in range(0, rows):
    #     user_input = input()
    #     current_row = user_input.split()
    #     input_arr.append(current_row)

    max_len = find_longest_adjacent_sequence(input_arr)
    print(max_len)


if __name__ == '__main__':
    main()
