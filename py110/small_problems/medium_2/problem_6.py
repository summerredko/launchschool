# Write a function that computes the difference between 
# the square of the sum of the first count positive integers 
# and the sum of the squares of the first count positive integers.

# Calculate the sum of the first count integers.
# Square that sum.
# Calculate the sum of the squares of the first count integers.
# Return the difference between the two values computed.

def sum_int(num):
    sum_int = 0
    for n in range(num+1):
        sum_int += n
    sum_int *= sum_int

    return sum_int

def sum_squares(num):
    sum_sq = 0
    for n in range(num+1):
        sum_sq += n ** 2
    return sum_sq

def sum_square_difference(num):
    sum_of_integers = sum_int(num)
    sum_of_squares = sum_squares(num)
    result = sum_of_integers - sum_of_squares

    return result



print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
