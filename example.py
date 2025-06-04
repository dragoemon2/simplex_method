from simplex_method import Dictionary

basis = [4, 5, 6]
unbasis = [1, 2, 3]

# シンプレックス表
tableau = [
    [0, -1, 4, -7],  # z
    [2, 1, -4, 0],   # x_4
    [3, 0, 1, -2],   # x_5
    [5, -1, 4, -1]   # x_6
]

dictionary = Dictionary(basis, unbasis, tableau)
dictionary.simplex_method(print_progress=True)