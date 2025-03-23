# P:
# Write a function that takes in three angles of a triangle and return their classification.

# E:
# Input: integer
# Output: string

# One angle is exactly 90 degrees = right
# All angles are less than 90 degrees = acute
# One angle is greater than 90 degrees = obtuse

# The sum of all angles must be exactly 180 degrees and greater than 0


# D:
# Integer
# List
# String


# A:
# Take in three integers are arguments.
# Add integers to a list.
# Loop through the list.
# If the sum is greater than 180 = invalid
# If an integer is 0 or less = invalid
# If one integer is 90 = right
# If all integers are less than 90 = acute
# If one integer is greater than 90 = obtuse


def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    angle_count = sum(angles)

    for angle in angles:
        if angle_count == 180 and angle == 90 and angle != 0:
            return "right"
        
        if angle_count == 180 and angle > 90 and angle != 0:
            return "obtuse"
        
        if angle == 0:
            return "invalid"
        

    if angle_count != 180:
        return "invalid"
    
    if angle1 and angle2 and angle3 < 90:
        return "acute"
    
    
        
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
