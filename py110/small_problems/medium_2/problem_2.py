# P:
# Write a function that takes the length of three sides of a triangle an return it's classification

# E:
# All three sizes are equal = Equilateral
# Two sides are equal and third not = Isosceles
# All three not equal = Scalene

# If two shortest sides not greater than longest or length less than 0 = invalid

# D:
# String

# A:
# Take in three integers are arguments
# If two shortest sides not greater than longest, return invalid
# If any side less than 1, return invalid
# If all three integers are equal, return equilateral
# If two sides are equal, return isosceles
# If all three different and greater than 0, return scalene

from collections import Counter


def triangle(side1, side2, side3):
    sides = [side1, side2, side3]

    # Check for invalid sides (zero or negative)
    if any(side <= 0 for side in sides):
        return "invalid"

    # Check for triangle inequality theorem
    if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
        return "invalid"

    # Check for equilateral
    if side1 == side2 == side3:
        return "equilateral"

    # Check for isosceles
    if len(set(sides)) == 2:
        return "isosceles"

    # If none of the above, it must be scalene
    return "scalene"
    






print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
