"""Horse gait"""

# n = 8
# w = []
# w.extend(input("enter the location of the knight (example c5) >>"))
# x, y = [i for i in w]
# m = 'abcdefgh'
# x = m.index(x)
# y = int(y) - 1
# matrix = [['. '] * n for i in range(n)]
# matrix[y][x] = 'N '
#
# for i in range(n):
#     for j in range(n):
#         if (i - y) ** 2 + (j - x) ** 2 == 5:
#             matrix[i][j] = '* '
# matrix.reverse()
#
# for row in matrix:
#     print(*row)

import numpy as np


def horse_gait():
    n = 8
    w = input("Enter the location of the knight (example c5) >>")
    m = 'abcdefgh'
    f = '12345678'

    if len(w) != 2 or not w[0] in m or not w[1] in f:
        print(f'You entered an incorrect location: {w}')

    else:
        rows, cols = w
        letters = ('  ', 'a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'g ', 'h ', '  ')
        digits = ('  ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '  ')
        x = m.index(rows)
        y = int(cols) - 1
        matrix = np.full((n, n), '. ')
        matrix[y][x] = 'N '

        indices = np.indices((n, n))
        distances = np.sqrt((indices[0] - y) ** 2 + (indices[1] - x) ** 2)
        mask = np.logical_and(distances > 0, distances == np.sqrt(5))
        matrix[mask] = '* '

        matrix = np.flipud(matrix)
        border_size = 1

        new_rows = n + 2 * border_size
        new_cols = n + 2 * border_size

        n_matrix = np.full((new_rows, new_cols), '. ')
        n_matrix[0] = letters

        for i, digit in enumerate(digits[-2:0:-1]):
            n_matrix[i+1][-1] = digit
            n_matrix[i + 1][0] = digit

        n_matrix[-1] = letters
        n_matrix[border_size:border_size + n, border_size:border_size + n] = matrix

        for row in n_matrix:
            print(*row)


if __name__ == '__main__':
    horse_gait()
