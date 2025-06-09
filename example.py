from simplex_method import Dictionary

basis = [4, 5, 6]
unbasis = [1, 2, 3]

# シンプレックス表
tableau = [
    [0, -1, -1, -1],  # z
    [2, -1, 1, 2],   # x_4
    [4, -2, 1, 2],   # x_5
    [3, 1, -2, -5]   # x_6
]

dictionary = Dictionary(basis, unbasis, tableau)
dictionary.simplex_method(print_progress=True)