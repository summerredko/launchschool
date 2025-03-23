# P:
# Write a function that transposes a 3x3 matrix

# E:
# Input: list
# Output: list
# 	Do not mutate the original list.

# D:
# List

# A:
# Take a list with nested lists as an argument.
# Loop through the outer list
# Loop through the inner lists
# Copy lst[0] for each sublist into a new list 
# Repeat until end of list

# def transpose(matrix):
#     transposed = []
#     new_rows_count = len(matrix[0])

#     for _ in range(new_rows_count):
#         transposed.append([])

#     for row_idx in range(len(matrix)):
#         for col_idx in range(len(matrix[row_idx])):
#             transposed[col_idx].append(matrix[row_idx][col_idx])

#     return transposed


def transpose(matrix: list):
    return([list(row) for row in zip(*matrix)])

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)
print(new_matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
