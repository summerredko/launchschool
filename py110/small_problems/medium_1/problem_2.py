# P:
# Write a function that rotates the last count digits of a number. 
# To perform the rotation, move the first of the digits that you want to 
# rotate to the end and shift the remaining digits to the left.

# E:
# Remove the element at index to end of list

# D:
# List

# A:
# Convert to string and then list.
# Extract the digit.
# Append to the end of the list.
# Rejoin string
# Return new number.

def rotate_list(string):
    return string[1:] + string[0]

def rotate_rightmost_digits(number, count):
    # string = str(number)
    # lst = []
    # for char in string:
    #     lst.append(char)
    # sublist = lst[-count:]
    # swap = sublist.pop(0)
    # lst = lst[:-count] + sublist 
    # lst += swap
    # new_string = ''.join(lst)
    # result = int(new_string)

    string = str(number)
    substring1 = string[:-count]
    substring2 = string[-count:]
    result = substring1 + rotate_list(substring2)
    return int(result)




print(rotate_rightmost_digits(735291, 2))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
