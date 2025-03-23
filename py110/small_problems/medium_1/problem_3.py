# Take the number 735291 and rotate it by one digit to the left, getting 352917. 
# Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
# Keep the first two digits fixed in place and rotate again to get 321759. 
# Keep the first three digits fixed in place and rotate again to get 321597. 
# Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 

count = 1
def rotate_list(string):
    return string[1:] + string[0]

def rotate_rightmost_digits(number, count):
    string = str(number)
    substring1 = string[:-count]
    substring2 = string[-count:]
    result = substring1 + rotate_list(substring2)
    return int(result)

def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number                 

# 735291
# 


# print(max_rotation(735291))

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
